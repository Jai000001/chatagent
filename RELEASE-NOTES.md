<!--
Release Notes

This document outlines the changes made in the current release. 
It includes bug fixes, new features, and updates to the existing functionality.
-->

# Release Notes

## Version 0.1.57

### Changes and Fixes

- **Added**: changed n_results to 15 in query_documents.

## Version 0.1.56

### Changes and Fixes

- **Added**: added url_uuid handling for delete API and changed get_collection_data function in chromadb handler.

## Version 0.1.55

### Changes and Fixes

- **Added**: added batch wise deletion, activation and deactivation for documents.

## Version 0.1.54

### Changes and Fixes

- **Added**: made changed for callback to java server api for no task id and java server url.

## Version 0.1.53

### Changes and Fixes

- **Added**: Added callback to java server api for no task id.

## Version 0.1.52

### Changes and Fixes

- **Added**: Fixed error handling for website scraping.
- **Added**: Fixed default prompt for answering questions.

## Version 0.1.51

### Changes and Fixes

- **Added**: Added api that creates collection using client id.
- **Added**: Implemented streaming response for question-answering.

## Version 0.1.50

### Changes and Fixes

- **Added**: Changed openai API key.

## Version 0.1.49

### Changes and Fixes

- **Added**: Fixed prompt issue for handling questions outside of context.

## Version 0.1.48

### Changes and Fixes

- **Added**: Changed progress response for website scraping and pdf url processing.

## Version 0.1.47

### Changes and Fixes

- **Added**: Added context awareness handling when user inputs context in the chat.
- **Added**: Changed flask production to development.

## Version 0.1.46

### Changes and Fixes

- **Added**: Added error handling for upload files, pdf url and website processing API.
- **Added**: Changed flask development to production.
- **Added**: Added uuid variable for website scraping API to handle duplication.

## Version 0.1.45

### Changes and Fixes

- **Added**: Updated the proposal prompt to handle response for html tags and humanized response.

## Version 0.1.44

### Changes and Fixes

- **Added**: added pagination to update hnsw for large datasets.

## Version 0.1.43

### Changes and Fixes

- **Added**: Added new prompt to handle proposal documents.
- **Added**: Changed word doc loader to use mammoth.
- **Added**: Changed error handling for get or create collection function for chromadb.

## Version 0.1.42

### Changes and Fixes

- **Added**: Added function to update old collection with hnsw parameters in chromadb handler.

## Version 0.1.41

### Changes and Fixes

- **Added**: Added hnsw in chromadb.
- **Added**: Added Cancel API functionalities.
- **Added**: Changed inactive/active API response.
- **Added**: Optimized resume parser.
- **Added**: Changed model to gpt-4o mini and retrieved results to 10. 

## Version 0.1.40

### Changes and Fixes

- **Added**: Removed slack integration.

## Version 0.1.39

### Changes and Fixes

- **Added**: Changed inactive/active API response.

## Version 0.1.38

### Changes and Fixes

- **Added**: Serialized json response for resume parser and changed the resume prompt for variables. 

## Version 0.1.37

### Changes and Fixes

- **Fixed**: Fixed word document loader for resume parser. 

## Version 0.1.36

### Changes and Fixes

- **Added**: Added error message for inactive/active API and delete source API .
- **Fixed**: Updated end time to show local time instead og gmt time 

## Version 0.1.35

### Changes and Fixes

- **Added**: Added task_id in form data for process pdf url API.

## Version 0.1.34

### Changes and Fixes

- **Added**: Added fromSlack key in question-answer API to handle plain text response.
- **Added**: Added timezone for the docker container 

## Version 0.1.33

### Changes and Fixes

- **Added**: Added dynamic threshold calculation for the results in the retriever function.

## Version 0.1.32

### Changes and Fixes

- **Added**: Changed Flask production setup to development setup.

## Version 0.1.31

### Changes and Fixes

- **Fixed**: Updated inactive/active (toggle source status) API where instead of deleting data, we are marking as inactive data.
- **Added**: Added incoming request logs for all APIs.
- **Added**: Added Flask production setup.

## Version 0.1.30

### Changes and Fixes

- **Added**: Added implementation for resume parser.

## Version 0.1.29

### Changes and Fixes

- **Fixed**: Fixed the system prompt for displaying sources and shortened the response.
- **Added**: Added task_id in form data for uploading doc and scraping website.

## Version 0.1.28

### Changes and Fixes

- **Fixed**: Fixed activating of document and website in inactive/active API.
- **Added**: Updated the openAI API key.
- **Added**: Updated the dockerfile to include a timeout

## Version 0.1.27

### Changes and Fixes

- **Fixed**: Updated system prompt for accuracy.
- **Fixed**: Fixed response for cost and total tokens for multiple document upload.
- **Added**: Added data size and end time in response for document upload and website scraping.

## Version 0.1.26

### Changes and Fixes

- **Fixed**: Fixed the system prompt for url sources.

## Version 0.1.25

### Changes and Fixes

- **Added**: Added 3 dynamic prompt templates - default, law and act, and ChatGPT like prompt.

## Version 0.1.24

### Changes and Fixes

- **Added**: Updated the system prompt.

## Version 0.1.23

### Changes and Fixes

- **Added**: Updated the system prompt.
- **Added**: added handling for reuploading of documents.

## Version 0.1.22

### Changes and Fixes

- **Added**: Updated the system prompt.
- **Added**: Updated source separation from chatbot response.

## Version 0.1.21

### Changes and Fixes

- **Added**: Updated the system prompt.
- **Added**: Added source separation from chatbot response.

## Version 0.1.20

### Changes and Fixes
- **Added**: Updated the system prompt.

## Version 0.1.19

### Changes and Fixes
- **Added**: Removed profanity checking and content moderation.

## Version 0.1.18

### Changes and Fixes
- **Fixed**: Fixed prompt for relevant context.

## Version 0.1.17

### Changes and Fixes
- **Fixed**: Added cost variable in response when unique chunks is empty.

## Version 0.1.16

### Changes and Fixes
- **Added**: Added hate speech detection, profanity checker and content moderation.
- **Fixed**: Resolved client ID issue with duplicate content.

## Version 0.1.15

### Changes and Fixes
- **Fixed**: Resolved duplicate content issue for website scraping.

## Version 0.1.14

### Changes and Fixes
- **Added**: To remove duplicate content in documents for embeddings.

## Version 0.1.13

### Changes and Fixes
- **Added**: Removed $ sign from the cost parameter.

## Version 0.1.12

### Changes and Fixes
- **Added**: Added embedding and LLM cost.
- **Added**: Updated the MAX_DEPTH and MAX_TIME for website scraping. 
- **Added**: Optimized the website scraping code.

## Version 0.1.11

### Changes and Fixes
- **Fixed**: Updated openai API key.

## Version 0.1.10

### Changes and Fixes
- **Added**: Updated response for inactive/active API.
- **Fixed**: Updated ChatPromptTemplate.

## Version 0.1.9

### Changes and Fixes
- **Added**: Updated response for website scraping.

## Version 0.1.8

### Changes and Fixes
- **Added**: Added process pdf urls API.

## Version 0.1.7

### Changes and Fixes
- **Added**: Added pdf document detection in urls.

## Version 0.1.6

### Changes and Fixes
- **Added**: Hardcoded the Department ID as "public".
- **Added**: Removed action as an array and kept as a string object in active/inactive API.

## Version 0.1.5

### Changes and Fixes
- **Added**: Manual slack integration.
- **Fixed**: Updated openai API key.

## Version 0.1.4

### Changes and Fixes
- **Added**: Implementation of client ID for resetting chromadb and fetching data collection.

## Version 0.1.3

### Changes and Fixes
- **Fixed**: Enchancement in prompt template (Context continuity for multiple sources including langchain chat history and when no sources available returns default response)
- **Added**: Delete API using multiple source names and multiple department IDS.
- **Added**: Delete API using single document ID of the source.
- **Added**: Active and Inactive API using multiple sources and multiple deptartment IDs.
- **Added**: Updating of department ID API using multiple source names and multiple department IDS.
- **Added**: Start times, date and execution times for web scraping and file uploading.
- **Added**: Multiple department IDs as input for web scraping and file uploading APIs.

## Version 0.1.2

### Changes and Fixes
- **Fixed**: Enchancement in prompt template
- **Added**: Support multiple files extraction [PDF, DOC(X), PPT(X), TXT].
- **Added**: Login and Signup API.
- **Added**: Text to Audio and Audio to Text API.

## Version 0.1.1

### Changes and Fixes
- **Fixed**: Reset Chromadb Data API issues.
- **Fixed**: Question form was calling twice from index_main.html
- **Added**: Flask CORS support in the environment.
- **Updated**: Cleared chat history on reset of Chromadb data.
