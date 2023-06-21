# 📑 Documentation

## 📌 Description

Vicuna is an open-source chatbot, fine-tuned on LLaMA using conversations from ShareGPT. Developed collaboratively by a team from UC Berkeley, CMU, Stanford, and UC San Diego, this auto-regressive language model aims to advance research in large language models and chatbots. Primarily designed for researchers and hobbyists in AI and NLP, the model undergoes preliminary evaluations using diverse questions and GPT-4 for output judgment. The current model has been 4-bit quantized using ggml framework <a href='https://vicuna.lmsys.org/' target='_blank'>Learn More</a>.

## 📒 Example Usage

### 1️⃣ Prompt: Can you explain what is a large language model?

```markdown
Sure! A large language model is a class of machine learning models that are trained on very large amounts of text data. The goal of training these models is to create a representation of human language that can be used for various natural language processing tasks, such as text generation, question- Answering and sentiment analysis. These models typically consist of several layers of neural networks, with each layer representing a different aspect of language (e.g., word meaning, syntax, context). As the model gets larger, it has the ability to learn more abstract representations of language that are more representative of human language understanding.
```

### 2️⃣ Prompt: Can you give some examples applications?

```markdown
Large language models have a wide range of applications in natural language processing, here are a few examples:

1. Text generation: Large language models can be used to generate text that sounds like it was written by a human, such as chatbot responses or summaries of long articles.
2. Question-Answering: Large language models can be trained to answer questions based on the information in a large dataset of text. This is often used in virtual assistants and search engines.
3. Sentiment analysis: Large language models can be used to understand the sentiment behind a piece of text, such as a customer review or social media post.
4. Translation: Large language models can be trained to translate text from one language to another, using large amounts of training data from both languages.
5. Dialogue System: Large language model can help in building dialogue system which can have human-like conversations with users.
6. Language Modeling: Large language models are used for language modeling task where they are able to mimic the way humans produce and process natural language.
```

### 3️⃣ Prompt: Are there any limitations?

```markdown
While large language models have many benefits, there are also some limitations that should be considered:

1. Large datasets required: Training a large language model requires access to vast amounts of text data, which can be difficult or expensive to obtain.
2. Computational resources required: Training and using large language models requires significant computational resources, which may not always be available.
3. Privacy concerns: Training large language models on personal data can raise privacy concerns. It is important to ensure that the data used for training is handled responsibly and ethically.
```

### 4️⃣ Prompt: Summarize the above in two sentences.

```markdown
Large language models have many benefits, but also require access to vast amounts of text data, computational resources, and should be trained with responsible and ethical handling of personal data.
```

### 5️⃣ Prompt: Write me a story about a superstar.

```markdown
Once upon a time, there was a young man named Jack who dreamed of becoming a superstar. Despite facing numerous obstacles and setbacks, he never gave up on his goal.

One day, an opportunity came knocking at his door. A record label scout approached him with a contract, recognizing his talent and potential. Jack was overjoyed and eagerly signed the deal.

As his career began to take off, Jack found himself traveling all around the world on tour. He met many other talented musicians and artists along the way, but none as kind and generous as his
```

## 🛠️ Technical Details

### 🔢 Default Parameters

For our experiments, we have been using the following parameters:

```python
temperature=0.2
top_p=0.95
stop=[]
max_tokens=256
repeat_penalty=1.1
```

### 📏 Inference Benchmarks

### 🔎 Quality Benchmarks

For more information concerning Vicuna evaluation method you can refer to <a href='https://github.com/lm-sys/FastChat/tree/main/fastchat/eval' target='_blank'></a>.

### 🚀 Serving Details

In order to expose the service we are currently using FastAPI and llama-cpp-python library <a href='https://abetlen.github.io/llama-cpp-python/' target='_blank'></a> which is compatible with all ggml models.

```python
llama-cpp-python==0.1.43
```

### ⚪️ Embeddings

The current model supports Embeddings generation too. Another endpoint is exposed for this purpose. You can check out the documentation for each container to see how to use it at `http://IP:PORT/docs` or at our public services Open API doc at <a href='https://mock.prem.ninja/docs' target='_blank'></a>

### 🦜🔗 Getting Started (using LangChain)

```python
!pip install langchain
!pip install openai

import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

os.environ["OPENAI_API_KEY"] = "random-string"

chat = ChatOpenAI(openai_api_base="http://localhost:8111/api/v1", max_tokens=128)

messages = [
    HumanMessage(content="Can you explain what is a large language model?")
]
chat(messages)
```

## 📜 License

The model is a research preview intended for non-commercial use only, subject to the model License of LLaMA, Terms of Use of the data generated by OpenAI, and Privacy Practices of ShareGPT. 