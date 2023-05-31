# Documentation

## Description

Qdrant is a vector similarity search engine designed for storing, searching, and managing points along with their respective payloads. Built with an emphasis on extensive filtering, it is particularly beneficial for neural network matching, semantic-based matching, and faceted search. Qdrant offers various deployment options including local mode, on-premise server deployment, and Qdrant Cloud, each catering to different use-case scenarios. [Learn More](https://qdrant.tech/documentation/)

## Example Usage

The service can be used with Langchain or the official qdrant python client (https://github.com/qdrant/qdrant). Below you can find an example using the service with Langchain. In the code snippet, we are assuming that you are using all-miniLM-l6-v2 model for embeddings generation and the service is running locally on port 8001.

```python

!pip install qdrant-client

import os
import getpass
import openai

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

url = "http://localhost:6333"
qdrant = Qdrant.from_documents(
    docs, embeddings, 
    url, prefer_grpc=True, 
    collection_name="my_documents",
)

query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.similarity_search(query)

print(found_docs[0].page_content)
```
