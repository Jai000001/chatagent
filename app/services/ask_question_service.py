from fastapi import HTTPException
from typing import Optional
from langchain_openai import ChatOpenAI
from app.core.app_config import app_config
from app.core.logger import Logger
logger = Logger.get_logger(__name__)
 
llm = ChatOpenAI(model=app_config.MODEL, temperature=0.7)

class AskQuestionService:
    def __init__(self):
        from app.core.chat_memory_store import chat_memories
        self.chat_memories = chat_memories

    async def ask_question(self, request, session_id: Optional[str], client_id: str, prompt_type: str, fromSlack: str, question: str):
        source = ""
        try:
            from app.adapters.database.qdrantdb_handler import QdrantDBHandler
            from app.prompts.prompt_factory import PromptFactory
            from datetime import datetime, timezone
            from app.utils.shared_utils import log_request_details, clean_answer
            from langchain.schema import AIMessage
            from langchain.memory import ConversationBufferMemory
            import asyncio
            import re
            import html

            qdrant_handler = QdrantDBHandler()
            prompt_factory = PromptFactory()

            fromSlack = str(fromSlack).strip().lower() == "true"
            
            dept_id = "public"
            if not client_id or not dept_id:
                raise HTTPException(status_code=400, detail="Client ID and Department ID cannot be None.")

            await log_request_details(request, dept_ids=dept_id)

            retriever = await qdrant_handler.query_documents(question, client_id, dept_id)
            logger.info(f"Retrieved documents: {len(retriever.get('documents', []))} docs")

            formatted_results = []
            documents = retriever.get('documents', [])
            metadatas = retriever.get('metadatas', [])
            for doc, metadata in zip(documents, metadatas):
                if not isinstance(metadata, dict):
                    logger.warning(f"Expected metadata to be dict but got {type(metadata)}: {metadata}")
                    metadata = {}
                if doc:
                    formatted_results.append(f"Source:{metadata.get('source', 'Unknown')}<br />{doc}")
            context_text = "\n".join(formatted_results) if formatted_results else ""

            if not context_text:
                prompt_template = prompt_factory.langchain_prompt_default()
            else:
                prompt_template = prompt_factory.langchain_prompt(prompt_type)
            # chat_history = self.chat_memories[session_id].chat_memory.messages if session_id in self.chat_memories else []

            if session_id in self.chat_memories:
                memory_entry = self.chat_memories[session_id]
                memory_entry["last_used"] = datetime.now(timezone.utc)
                chat_history = memory_entry["chat_memory"].chat_memory.messages
            else:
                self.chat_memories[session_id] = {
                    "chat_memory": ConversationBufferMemory(return_messages=True),
                    "last_used": datetime.now(timezone.utc),
                    "client_id": client_id
                }
                chat_history = []

            inputs = {
                "input": question,
                "context": context_text,
                "chat_history": chat_history
            }

            # Create a RunnableSequence with the updated prompt and the LLM
            question_answer_chain = prompt_template | llm

            try:
                # Get the answer from the LLM using the full input
                response = await asyncio.to_thread(question_answer_chain.invoke, inputs)
                source_list = ""
                lines = response.content.split('\n')
                for line in lines:
                    if line.startswith('Source:'):
                        source_list = line.split('Source: ')[-1].strip()
                        break
                # Safe access to attributes
                response_metadata = getattr(response, 'response_metadata', {})
                usage_metadata = getattr(response, 'usage_metadata', {})

                # Extract values safely using get method with default values
                completion_tokens = response_metadata.get('token_usage', {}).get('completion_tokens', None)
                prompt_tokens = response_metadata.get('token_usage', {}).get('prompt_tokens', None)
                total_tokens_response = response_metadata.get('token_usage', {}).get('total_tokens', None)

                input_tokens = usage_metadata.get('input_tokens', None)
                output_tokens = usage_metadata.get('output_tokens', None)
                total_tokens_usage = usage_metadata.get('total_tokens', None)

                input_cost = (prompt_tokens or input_tokens or 0) * (app_config.INPUT_RATE_PER_1K_TOKENS / 1000)
                output_cost = (completion_tokens or output_tokens or 0) * (app_config.OUTPUT_RATE_PER_1K_TOKENS / 1000)
                total_cost = input_cost + output_cost
                
                # Convert AIMessage to string if needed
                if isinstance(response, AIMessage):
                    answer = response.content
                else:
                    answer = str(response)
                answer = clean_answer(answer)
                
                # Update memory with the current question and answer using save_context
                self.chat_memories[session_id]["chat_memory"].save_context(
                    {"input": question},  # Human message
                    {"output": answer}    # AI response
                ) 
                
                # Convert HTML to plain text if slack is True
                if fromSlack:
                    # Remove common HTML tags
                    answer = re.sub(r'<[^>]+>', '', answer)
                    # Convert special HTML entities
                    answer = html.unescape(answer)
                    # Remove extra whitespace
                    answer = ' '.join(answer.split())

                from app.services.service_utils import split_answer_and_source
                answer, source = await split_answer_and_source(answer, fromSlack)
                
            except Exception as e:
                logger.error(f"Error during question answering: {e}")
                answer = "An error occurred while processing the question."
                total_cost = 0
            logger.info(f"\n\nChat history for session {session_id}: {self.chat_memories[session_id]['chat_memory'].buffer}")

            # Log the extracted values
            logger.info(f"\nResponse Details:\n"
                        f"{{'session_id': {session_id},\n"
                        f"'client_id': {client_id},\n"
                        f"'dept_id': {dept_id},\n"
                        f"'prompt_type': {prompt_type},\n"
                        f"'response': {response.content},\n"
                        f"'question': {question},\n"
                        f"'answer': {answer},\n"
                        f"'input_tokens': {input_tokens},\n"
                        f"'output_tokens': {output_tokens},\n"
                        f"'total_tokens_usage': {total_tokens_usage},\n"
                        f"'total_cost': {total_cost:.6f},\n"
                        f"'fromSlack': {fromSlack}}}\n")
            
            return {
                "session_id": session_id,
                "question": question,
                "answer": answer,
                "source": source,
                "client_id": client_id,
                "dept_id": dept_id,
                "cost": f"{total_cost:.6f}"
            }

        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"ask question error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error while processing question.")
        
