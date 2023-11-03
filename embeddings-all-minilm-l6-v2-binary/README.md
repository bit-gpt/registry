# 📑 Documentation

## 📌 Description

All-MiniLM-L6-v2 is a sentence-transformers model designed to map sentences and paragraphs to a 384-dimensional dense vector space, ideal for clustering or semantic search tasks. Developed during <a href='https://huggingface.co/' target='_blank'>Hugging Face</a>'s Community week, this model is fine-tuned on a 1B sentence pairs dataset with a contrastive learning objective. It excels in encoding short texts, capturing semantic information, and is useful for information retrieval, clustering, or sentence similarity tasks. <a href='https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2' target='_blank'>Learn more</a> 🚀.

## 👇 Getting Started

The service is compatible with 🦜🔗<a href='https://github.com/hwchase17/langchain' target='_blank'>LangChain</a> and follows OpenAI <a href='https://platform.openai.com/docs/api-reference' target='_blank'>API request-response</a> format. If you haven't already, you will need to install :

* `langchain` ➡️ <a href='https://pypi.org/project/langchain/' target='_blank'>pip install</a>.
* `tiktoken` ➡️ <a href='https://pypi.org/project/tiktoken/' target='_blank'>pip install</a>.
* `openai` ➡️ <a href='https://pypi.org/project/openai/' target='_blank'>pip install</a>.

## ⚒️ Usage

👉 Find an example for using the service with 🦜🔗 LangChain below:

```python
import os

from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "random-string"

embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:8444/v1")
text = "Prem is an easy to use open source AI platform."
query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text])
```


Also check the official sentence transformers <a href='https://www.sbert.net/' target='_blank'>documentation</a>. It provides extensive examples and detailed information for using the model.

## 👀 Intended Uses
The model is meant to be used as an encoder for single sentences and short paragraphs. Given an input text, it outputs a vector that captures the semantic information. You can use the sentence vector generated for information retrieval, clustering, or sentence similarity tasks.

By default, input text longer than 256-word pieces is truncated.

## 🔎 Evaluation Results
For an automated evaluation of this model, see the Sentence Embeddings Benchmark <a href='https://seb.sbert.net' target='_blank'>page</a>.

## ⚖️ License

The model is published under <a href='https://www.apache.org/licenses/LICENSE-2.0' target='_blank'>Apache License 2.0</a>.
