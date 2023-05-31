# Documentation

## Description

Redis, short for Remote Dictionary Server, serves as a multifunctional in-memory data structure store. It functions as a distributed key-value database, cache, and message broker, all operating in-memory for high-speed data access. With optional durability, Redis ensures data persistence despite potential system failures. Learn more https://redis.com/solutions/use-cases/vector-database/.

## Example Usage

The service can be used with Langchain. You can check the official documentation at this link: https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/redis.html. In the code snippet, we are assuming that you are using all-miniLM-l6-v2 model for embeddings generation and the service is running locally on port 8001.

```python

!pip install redis

import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.redis import Redis

from langchain.document_loaders import TextLoader

loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

rds = Redis.from_documents(docs, embeddings, redis_url="redis://localhost:6379",  index_name='link')
```