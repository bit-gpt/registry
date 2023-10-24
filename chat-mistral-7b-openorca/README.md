# 📑 Documentation

## 📌 Description
The Mistral 7B OpenOrca is a model built by finetuning  <a href='https://huggingface.co/mistralai/Mistral-7B-v0.1' target='_blank'>Mistral-7B-v0.1</a> on the  
<a href='https://huggingface.co/datasets/Open-Orca/OpenOrca' target='_blank'>OpenOrca dataset</a>.


## 📒 Example Usage

Following are a few example generations with `max_token=64` set.

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \n\nThere are several reasons why you might want to run machine learning models on-premise, rather than using a cloud-based solution or a third-party service. Here are some of the key benefits:\n\n1. Security and privacy: Running machine learning models on-premise allows you to

### 2️⃣ Prompt: How do I run my models on-premise?

> \n\nTo run your models on-premise, you will need to follow these steps:\n\n1. Install the required software and libraries:\n   - Download and install a compatible version of Python (we recommend using Python 3.6 or later).\n   - Install the necessary libraries for running your

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \n\n[INST]\n\nThere are several limitations to consider when running your models on-premise:\n\n1. Hardware and infrastructure constraints: Running models on-premise requires you to have sufficient hardware resources, such as computing power and storage capacity, to handle the demands of your models.

### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

> \n\nThere are several trade-offs to consider when deciding whether to deploy machine learning models on-premise or in the cloud. Here's a list of some key factors:\n\n1. **Cost:** On-premise deployment can be more expensive, as it requires investing in hardware, software

## 🛠️ Technical Details

### 🦜🔗 Getting Started with Langchain

```bash
pip install langchain openai
```

It can be run simply using the langchain library as shown below:

```python
import os
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "random-string"

chat = ChatOpenAI(openai_api_base="http://localhost:8446/v1", max_tokens=128)
messages = [HumanMessage(content="Why do I need to run machine learning models on-premise?")]
print(chat(messages))

# output:
```

For using it in a chat setting we recommend using a Chat Prompt Template as shown below:
    
```python

import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "random-string"

chat_template = """
You are an AI assistant in a conversational setting.
Provide a conversational answer to any question an User asks. Be original, concise, accurate and helpful.
===================

User: {user_message}
Assistant:"""
prompt = PromptTemplate(
    input_variables=["user_message"],
    template=chat_template,
)

user_message = "Why do I need to run machine learning models on-premise?"

chat = ChatOpenAI(openai_api_base="http://localhost:8446/v1", max_tokens=128)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

```

### 🔎 Quality Benchmarks

### 🚫 Limitations and Biases

## 📜 License
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.