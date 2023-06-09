# Documentation

## Description

All-MiniLM-L6-v2 is a sentence-transformers model designed to map sentences and paragraphs to a 384-dimensional dense vector space, ideal for clustering or semantic search tasks. Developed during Hugging Face's Community week, this model is fine-tuned on a 1B sentence pairs dataset with a contrastive learning objective. It excels in encoding short texts, capturing semantic information, and is useful for information retrieval, clustering, or sentence similarity tasks.

## Getting Started

The service is compatible with Langchain and more specifically it follows OpenAI API request / response format. Below you can find an example for using the service with Langchain.

```python
import os

from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "random-string"

embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:8444/api/v1")
text = "Prem is an easy to use open source AI platform."
query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text])
```

You can also check the official sentence transformers documentation at https://www.sbert.net/. It provides extensive examples and detailed information for using the model.

## License

The model is under Apache License.
