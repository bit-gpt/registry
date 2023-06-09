# Documentation

## Description

Qdrant is a vector similarity search engine designed for storing, searching, and managing points along with their respective payloads. Built with an emphasis on extensive filtering, it is particularly beneficial for neural network matching, semantic-based matching, and faceted search. Qdrant offers various deployment options including local mode, on-premise server deployment, and Qdrant Cloud, each catering to different use-case scenarios. [Learn More](https://qdrant.tech/documentation/)

## Getting Started

The service can be used with Langchain or the official qdrant python client (https://github.com/qdrant/qdrant). Below you can find an example using the service with Langchain. In the code snippet, we are assuming that you are using all-miniLM-l6-v2 model for embeddings generation and the service is running locally on port 8001.

```python

!pip install qdrant-client

import os

from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.vectorstores import Qdrant
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "random-string"

doc1 = Document(page_content="Prem is an easy to use open source AI platform. With Prem you can quickly build provacy preserving AI applications.")
doc2 = Document(page_content="""
Prem App

An intuitive desktop application designed to effortlessly deploy and self-host Open-Source AI models without exposing sensitive data to third-party.

""")
doc3 = Document(page_content="""
Prem Benefits

Effortless Integration
Seamlessly implement machine learning models with the user-friendly interface of OpenAI's API.

Ready for the Real World
Bypass the complexities of inference optimizations. Prem's got you covered.

Rapid Iterations, Instant Results
Develop, test, and deploy your models in just minutes.

Privacy Above All
Your keys, your models. We ensure end-to-end encryption.

Comprehensive Documentation
Dive into our rich resources and learn how to make the most of Prem.

Preserve Your Anonymity
Make payments with Bitcoin and Cryptocurrency. It's a permissionless infrastructure, designed for you.
""")

# Using sentence transformers all-MiniLM-L6-v2
embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:8001/api/v1")

# Using locally running Qdrant
url = "http://localhost:6333"

vectorstore = Qdrant.from_documents(
    [doc1, doc2, doc3], 
    embeddings, 
    url=url, 
    collection_name="prem_collection_test",
)

query = "What are Prem Benefits?"
docs = vectorstore.similarity_search(query)
print(docs[0].page_content)
```
