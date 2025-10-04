import pandas as pd
from app.core.logger import Logger
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
import html

logger = Logger.get_logger(__name__)

class TXTParser:
    def __init__(self):
        pass

    async def load_async(self, file_path):
        # Step 1: Load file using LangChain TextLoader
        try:
            loader = TextLoader(file_path, autodetect_encoding=True)
            docs = loader.load()
        except UnicodeDecodeError:
            logger.warning(f"TextLoader failed with autodetect, retrying with utf-8")
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()

        # Step 2: Parse and serialize content into LangChain Documents
        text = "\n".join(doc.page_content for doc in docs)
        docs = self._parse_and_serialize(text, file_path)
        return "\n".join(doc.page_content for doc in docs)
        # return docs

    def _is_likely_table(self, lines, sample_size=20):
        """Check if content resembles a table based on delimiters and consistent columns."""
        # Test tab delimiter first since your data is tab-separated
        delimiters = [("\t", r"\t"), (",", r","), ("|", r"\|")]
        max_columns = 0
        best_delim = None
        best_delim_char = None
        
        for delim_char, delim_pattern in delimiters:
            column_counts = []
            for i, line in enumerate(lines[:sample_size]):
                if line.strip():
                    try:
                        # Count actual delimiter occurrences
                        delimiter_count = line.count(delim_char)
                        if delimiter_count > 0:
                            columns = line.split(delim_char)
                            # Clean empty columns at the end
                            while columns and not columns[-1].strip():
                                columns.pop()
                            if len(columns) > 1:
                                column_counts.append(len(columns))
                                logger.debug(f"Line {i+1}: found {len(columns)} columns with delimiter '{delim_char}'")
                    except Exception as e:
                        logger.debug(f"Failed to parse line {i+1} with delimiter '{delim_char}': {e}")
                        continue
            
            # Check consistency and column count
            if column_counts:
                most_common_count = max(set(column_counts), key=column_counts.count)
                consistency = column_counts.count(most_common_count) / len(column_counts)
                
                # Prefer tab delimiter and require good consistency
                if consistency >= 0.7 and most_common_count > max_columns:
                    max_columns = most_common_count
                    best_delim = delim_pattern
                    best_delim_char = delim_char
                    
        if max_columns > 1:
            logger.info(f"Detected table with delimiter '{best_delim_char}' ({best_delim}), {max_columns} columns")
            return True, best_delim, max_columns, best_delim_char
        logger.info("No table detected")
        return False, None, 0, None

    def _safe_str_conversion(self, value):
        """Safely convert any value to string, handling None, NaN, and other edge cases."""
        if value is None:
            return ""
        if pd.isna(value):
            return ""
        # Handle various types that might not be strings
        if isinstance(value, (int, float, bool)):
            return str(value)
        if isinstance(value, (list, dict, tuple)):
            return str(value)
        # Convert to string and strip whitespace
        result = str(value).strip()
        # Ensure we return a proper string
        if not isinstance(result, str):
            result = str(result)
        return result

    def _parse_and_serialize(self, text, file_path):
        """Parse text and serialize tables with headers per row, returning LangChain Documents."""
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if not lines:
            return [Document(page_content="Empty file", metadata={"source": file_path})]

        # Check for table structure
        table_result = self._is_likely_table(lines)
        is_table, delimiter, expected_columns, delimiter_char = table_result
        docs = []

        if not is_table:
            # Text-only: Create a Document for each line
            logger.info("Processing as text-only content")
            return [Document(page_content=self._safe_str_conversion(line), metadata={"source": file_path}) for line in lines]

        # Process as table
        logger.info(f"Processing as table with delimiter '{delimiter_char}' and {expected_columns} expected columns")
        
        # Find header line and determine actual structure
        header_line = None
        header_index = -1
        actual_column_count = 0
        
        # Check the actual structure of the first few data rows (not just column count)
        data_rows_sample = []
        for i, line in enumerate(lines[1:6], 1):  # Skip potential header, check next 5 lines
            if line.strip():
                columns = line.split(delimiter_char)
                data_rows_sample.append((i, len(columns), columns))
        
        if data_rows_sample:
            # Use the most common column count from data rows
            column_counts = [count for _, count, _ in data_rows_sample]
            actual_column_count = max(set(column_counts), key=column_counts.count)
            logger.info(f"Data rows have {actual_column_count} columns on average")
            
            # Log some sample data structure
            for i, count, cols in data_rows_sample[:3]:
                logger.debug(f"Row {i} has {count} columns: {[col[:20] + '...' if len(col) > 20 else col for col in cols]}")
        
        # Now check if the first line (potential header) matches this structure
        if lines:
            potential_header = lines[0]
            header_columns = potential_header.split(delimiter_char)
            
            if len(header_columns) == actual_column_count:
                # Header matches data structure exactly
                header_line = potential_header
                header_index = 0
                logger.info(f"Header matches data structure with {actual_column_count} columns")
            elif len(header_columns) < actual_column_count:
                # Header has fewer columns - pad with generic names
                header_line = potential_header
                header_index = 0
                # Add missing column names
                missing_count = actual_column_count - len(header_columns)
                for i in range(missing_count):
                    header_columns.append(f"Column_{len(header_columns) + 1}")
                logger.info(f"Header padded from {len(potential_header.split(delimiter_char))} to {actual_column_count} columns")
                # Rebuild header line
                header_line = delimiter_char.join(header_columns)
            else:
                # Header has more columns than data - use as is but warn
                header_line = potential_header
                header_index = 0
                logger.warning(f"Header has more columns ({len(header_columns)}) than data ({actual_column_count})")
            
            logger.info(f"Final header: {header_columns}")
        
        # Update expected_columns to match actual structure
        expected_columns = actual_column_count

        if not header_line:
            logger.warning("No valid header found; treating all lines as text")
            return [Document(page_content=self._safe_str_conversion(line), metadata={"source": file_path}) for line in lines]

        # Process the entire content as one table
        table_lines = []
        non_table_lines = []
        
        # Add header
        table_lines.append(header_line)
        
        # Process remaining lines with corrected column count
        for i, line in enumerate(lines):
            if i == header_index:  # Skip header as we already added it
                continue
                
            if line.strip():
                columns = line.split(delimiter_char)
                
                # Don't remove trailing columns - use actual column count
                # Only clean truly empty trailing columns (empty strings)
                while columns and columns[-1] == "":
                    columns.pop()
                    
                # Accept rows that match our actual column count (±1 for flexibility)
                expected_range = range(max(1, expected_columns - 1), expected_columns + 2)
                if len(columns) in expected_range:
                    table_lines.append(line)
                else:
                    logger.debug(f"Line {i+1} rejected: {len(columns)} columns (expected ~{expected_columns})")
                    non_table_lines.append(line)

        # Process the table manually without pandas to handle variable column counts
        if len(table_lines) > 1:  # Header + at least one data row
            try:
                # Get header columns from our processed header
                header_columns = header_line.split(delimiter_char)
                header_columns = [self._safe_str_conversion(col.strip()) for col in header_columns]
                
                # Ensure we have the right number of headers
                while len(header_columns) < expected_columns:
                    header_columns.append(f"Column_{len(header_columns) + 1}")
                
                logger.info(f"Processing with {len(header_columns)} header columns: {header_columns}")
                
                # Process each data row
                processed_rows = 0
                for line_idx, line in enumerate(table_lines[1:], 1):  # Skip header
                    if not line.strip():
                        continue
                        
                    try:
                        # Split by delimiter - preserve all columns
                        row_columns = line.split(delimiter_char)
                        
                        # Clean each column
                        cleaned_row_columns = []
                        for i, col in enumerate(row_columns):
                            cleaned_col = self._safe_str_conversion(col.strip()) if col is not None else ""
                            cleaned_row_columns.append(cleaned_col)
                        row_columns = cleaned_row_columns
                        
                        # Handle column count mismatches
                        if len(row_columns) < len(header_columns):
                            # Pad with empty strings
                            missing_count = len(header_columns) - len(row_columns)
                            row_columns.extend([""] * missing_count)
                            logger.debug(f"Row {line_idx}: padded from {len(row_columns)} to {len(header_columns)} columns")
                        elif len(row_columns) > len(header_columns):
                            # This shouldn't happen with our new logic, but handle it safely
                            logger.debug(f"Row {line_idx}: has {len(row_columns)} columns, using first {len(header_columns)}")
                            row_columns = row_columns[:len(header_columns)]
                        
                        # Create row string with all necessary safety checks
                        row_parts = []
                        for i, (header, value) in enumerate(zip(header_columns, row_columns)):
                            # Ensure header is a valid string
                            if isinstance(header, str) and header.strip():
                                clean_header = html.unescape(header).replace(":", "").strip()
                            else:
                                clean_header = f"column_{i+1}"
                            
                            # Ensure value is a string and clean it
                            clean_value = self._safe_str_conversion(value)
                            
                            if clean_value:  # Only include non-empty values
                                # Create the header:value pair with explicit string conversion
                                header_part = str(clean_header)
                                value_part = str(html.unescape(clean_value))
                                row_parts.append(f"{header_part}:{value_part}")
                        
                        # Create document only if we have valid content
                        if row_parts:
                            # Join with explicit string handling
                            row_str = ",".join(str(part) for part in row_parts)
                            
                            # Final validation before Document creation
                            if isinstance(row_str, str) and row_str.strip():
                                try:
                                    # Create document with explicit string page_content
                                    doc = Document(
                                        page_content=str(row_str),
                                        metadata={"source": str(file_path)}
                                    )
                                    docs.append(doc)
                                    processed_rows += 1
                                except Exception as doc_error:
                                    logger.error(f"Document creation failed at row {line_idx}: {doc_error}")
                                    logger.error(f"row_str type: {type(row_str)}")
                                    logger.error(f"row_str value: {repr(row_str[:200])}")
                                    # Fallback: try with basic string conversion
                                    try:
                                        fallback_content = str(line.strip())
                                        if fallback_content:
                                            docs.append(Document(
                                                page_content=fallback_content,
                                                metadata={"source": str(file_path)}
                                            ))
                                    except Exception as fallback_error:
                                        logger.error(f"Fallback also failed: {fallback_error}")
                            else:
                                logger.warning(f"Row {line_idx}: Invalid string content: {type(row_str)} - {repr(row_str)}")
                        else:
                            logger.debug(f"Row {line_idx}: No content to process")
                            
                    except Exception as row_error:
                        logger.warning(f"Failed to process row {line_idx}: {row_error}")
                        # Add problematic line as text document
                        line_content = self._safe_str_conversion(line)
                        if line_content:
                            docs.append(Document(page_content=line_content, metadata={"source": file_path}))
                
                logger.info(f"Successfully processed {processed_rows} table rows")
                    
            except Exception as e:
                logger.error(f"Failed to parse table: {e}")
                logger.debug(f"Table lines that failed: {table_lines[:3]}...")
                non_table_lines.extend(table_lines)

        # Add non-table lines as individual documents
        for line in non_table_lines:
            line_content = self._safe_str_conversion(line)
            if line_content:  # Only add non-empty lines
                docs.append(Document(page_content=line_content, metadata={"source": file_path}))

        if not docs:
            logger.warning("No documents created, adding empty file document")
            docs.append(Document(page_content="No valid content found", metadata={"source": file_path}))

        logger.info(f"Created {len(docs)} documents from file")
        return docs