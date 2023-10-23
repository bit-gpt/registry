# 📑 Documentation

## 📌 Description
The Mistral 7B Instruct is a model built by finetuning  <a href='https://huggingface.co/mistralai/Mistral-7B-v0.1' target='_blank'>Mistral-7B-v0.1</a>.

## 📒 Example Usage

Following are a few example generations with `max_token=64` set.

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> 1. Security and Privacy: On-premise machine learning allows organizations to maintain full control over their data, ensuring that sensitive information is not compromised during transmission or storage. This can be particularly important for industries such as healthcare or finance where data privacy regulations are strict.\n2. Customization: On-p

### 2️⃣ Prompt: How do I run my models on-premise?

> 1. Install the necessary software and dependencies for your model, such as Python, TensorFlow, or PyTorch.\n2. Download or transfer your trained model to your on-premise environment.\n3. Set up a server or cluster to run the model, either using existing infrastructure or by purchasing additional

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> 1. Limited scalability: On-premise infrastructure may have limited capacity to handle large volumes of data and computational workloads, which can limit the scalability of your models.\r\n\r\n2. Maintenance and upgrades: You are responsible for maintaining and upgrading the hardware and software infrastructure required

### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

> 1. Cost: On-premise deployment can be more expensive than cloud-based deployment, as it requires hardware and infrastructure to be purchased and maintained.\n2. Scalability: On-premise deployment may not be as scalable as cloud-based deployment, as it requires physical infrastructure to be added

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

chat = ChatOpenAI(openai_api_base="http://localhost:8448/v1", max_tokens=128)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8448/v1", max_tokens=128)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

```

### 🔎 Quality Benchmarks

### 🚫 Limitations and Biases

The Mistral 7B Instruct model serves as a quick demonstration of how the base model can be readily fine-tuned to achieve compelling performance. It lacks any moderation mechanisms. The developers anticipate engaging with the community on methods to refine the model's adherence to guardrails, enabling its deployment in environments necessitating moderated outputs.

## 📜 License
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.