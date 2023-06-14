# 📑 Documentation

## 📌 Description

All-MiniLM-L6-v2 is a sentence-transformers model designed to map sentences and paragraphs to a 384-dimensional dense vector space, ideal for clustering or semantic search tasks. Developed during [Hugging Face](https://huggingface.co/)'s Community week, this model is fine-tuned on a 1B sentence pairs dataset with a contrastive learning objective. It excels in encoding short texts, capturing semantic information, and is useful for information retrieval, clustering, or sentence similarity tasks. [Learn more](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) 🚀.

## 👇 Getting Started

The service is compatible with 🦜🔗[LangChain](https://github.com/hwchase17/langchain) and follows OpenAI [API request-response format](https://platform.openai.com/docs/api-reference). If you haven't already, you will need to install :

* `langchain` ➡️ [pip install](https://pypi.org/project/langchain/).
* `tiktoken` ➡️ [pip install](https://pypi.org/project/tiktoken/).
* `openai` ➡️ [pip install](https://pypi.org/project/openai/).

## ⚒️ Usage

👉 Find an example for using the service with 🦜🔗 LangChain below.

```python
import os

from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "random-string"

embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:8444/api/v1")
text = "Prem is an easy to use open source AI platform."
query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text])
```

Also check the official sentence transformers [documentation](https://www.sbert.net/). It provides extensive examples and detailed information for using the model.

## 👀 Intended uses
The model is meant to be used as an encoder for single sentences and short paragraphs. Given an input text, it outputs a vector that captures the semantic information. You can use the sentence vector generated for information retrieval, clustering, or sentence similarity tasks.

By default, input text longer than 256-word pieces is truncated.


## 🔎 Evaluation Results
For an automated evaluation of this model, see the Sentence Embeddings Benchmark: https://seb.sbert.net

## ⚖️ License

The model is published under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
  