from datetime import datetime
from langchain.memory import ConversationBufferMemory

# Structure: { session_id: { "chat_memory": ConversationBufferMemory, "last_used": datetime.now(timezone.utc), "client_id": str } }
chat_memories = {}