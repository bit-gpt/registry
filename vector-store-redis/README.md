# 📑 Documentation

## 📌 Description

Redis, short for Remote Dictionary Server, serves as a multifunctional in-memory data structure store. It functions as a distributed key-value database, cache, and message broker, all operating in-memory for high-speed data access. With optional durability, Redis ensures data persistence despite potential system failures. <a href='https://redis.com/solutions/use-cases/vector-database/' target='_blank'>Learn more</a> 🚀.

## 👇 Getting Started (Implementation)

The service can be used with Langchain. You can check the <a href='https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/redis.html' target='_blank'>official documentation</a>. In the code snippet below, weassume that you are using <a href='https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2' target='_blank'>`all-miniLM-l6-v2`</a> model for embeddings generation and the service is running locally on port 8001.

```python

!pip install redis

import os

from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.vectorstores.redis import Redis
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

# Using locally running Redis
url = "redis://localhost:6379"

rds = Redis.from_documents(docs, embeddings, redis_url=url,  index_name="prem_index_test")

query = "What are Prem Benefits?"
docs = vectorstore.similarity_search(query)
print(docs[0].page_content)
```

## 👀 Intended Uses
The model is meant to be used as an encoder for single sentences and short paragraphs. Given an input text, it outputs a vector that captures the semantic information. You can use the sentence vector generated for information retrieval, clustering, or sentence similarity tasks.

By default, input text longer than 256-word pieces is truncated.

<a href='https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/redis.html' target='_blank'>Learn more</a> 🚀.