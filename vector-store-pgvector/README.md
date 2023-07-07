
# 📑 Documentation

## 📌 Description

[PGVector](https://github.com/pgvector/pgvector) is an integration of PostgreSQL with vector-based operations and similarity searches. It allows you to store and query vector embeddings efficiently within the PostgreSQL database. PGVector is a powerful tool for building AI and ML applications that require similarity search capabilities. It supports:
- exact and approximate nearest neighbor search
- L2 distance, inner product, and cosine distance

Learn more about <a href='https://github.com/pgvector/pgvector' target='_blank'>PGVector here</a> 🚀.

## 👇 Getting Started (Implementation)

The service can be used with Langchain. You can check the [langchain pgvector documentation](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/pgvector) for detailed usage instructions. In the code snippet below, we assume that you have installed the required dependencies present in *Pre-requisites* step and are using `all-miniLM-l6-v2` model for embeddings generation and the service is running locally on port `8444`.



### Pre-requisites
> ⚠️ Currently there's a bug in the latest version of langchain. Hence to use the pgvector integration on non-openai embeddings, you need to install the version mentioned below. The issue can be tracked [here](https://github.com/hwchase17/langchain/issues/2219)
```bash
pip install pgvector tiktoken psycopg2-binary openai git+https://github.com/hwchase17/langchain.git@71d73a5f00dfd4e33a565762b7032d6b445d9bf6
```

```python

import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.vectorstores.pgvector import PGVector

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

# Using locally running PostgreSQL connection
CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver="psycopg2",
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="postgres",
)

# Create PGVector vectorstore instance
vectorstore = PGVector.from_documents(
    documents=[doc1, doc2, doc3],
    embedding=embeddings,
    connection_string=CONNECTION_STRING,
)

# Perform similarity search
query = "What are Prem Benefits?"
docs = vectorstore.similarity_search(query)
print(docs[0].page_content)
```
