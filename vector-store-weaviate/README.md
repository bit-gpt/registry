# 📑 Documentation

## 📌 Description

<a href='https://weaviate.io/' target='_blank'>Weaviate</a> is an open-source, cloud-native vector database designed to enable machine learning (ML) and artificial intelligence (AI) capabilities for your data. It's built to handle large-scale data storage and search operations, making it a powerful tool for data scientists and developers working with big data <a href='https://weaviate.io/developers/weaviate' target='_blank'>Learn more</a> 🚀.

## 👇 Getting Started (Implementation)

The service can be used with Langchain or the official weavaite python client (https://github.com/qdrant/qdrant). Below you can find an example using the service with Langchain. In the code snippet, we are assuming that you are using all-miniLM-l6-v2 model for embeddings generation and the service is running locally on port 8001.

```python

!pip install weaviate-client

import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.vectorstores import Weaviate

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
embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:8444/v1")

# Using locally running Weaviate
url = "http://localhost:8080"

vectorstore = Weaviate.from_documents(
    [doc1, doc2, doc3], 
    embeddings, 
    weaviate_url=url, 
    by_text=False,
)

query = "What are Prem Benefits?"
docs = vectorstore.similarity_search(query)
print(docs[0].page_content)
```