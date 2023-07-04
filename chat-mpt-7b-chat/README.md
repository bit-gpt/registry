# 📑 Documentation

## 📌 Description

MPT-7B-Chat is a chatbot-like model for dialogue generation. It was built by finetuning <a href='https://huggingface.co/mosaicml/mpt-7b' target='_blank'>MPT-7b</a> on the <a href='https://huggingface.co/datasets/jeffwan/sharegpt_vicuna' target='_blank'>ShareGPT-Vicuna</a>, <a href='https://huggingface.co/datasets/Hello-SimpleAI/HC3' target='_blank'>HC3</a>, <a href='https://huggingface.co/datasets/tatsu-lab/alpaca' target='_blank'>Alpaca</a>, <a href='https://huggingface.co/datasets/Anthropic/hh-rlhf' target='_blank'>HH-RLHF</a>, <a href='https://huggingface.co/datasets/victor123/evol_instruct_70k' target='_blank'>Evol-Instruct</a> datasets. This model was trained by MosaicML and follows a modified decoder-only transformer architecture.


## 💻 Hardware Requirements
To run the `mpt-7b-chat` service on Prem, you'll need access to a GPU:

You'd need an A100, A10, or V100.

### A100 GPUs
A100 GPUs are preferred for training all model sizes.

### A10 GPUs

### V100 GPUs
It can be ran on V100 GPUs.

> **Memory requirements**: 13.91 GB (13269 MiB).


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \n\nThere are several reasons why you might want to run machine learning models on-premise.  First, it gives you more control over the data and the model.  You can make sure that the data is clean and that the model is well-validated before you deploy it into production.  Second, it can help you meet compliance requirements.  If you’re working with sensitive data, you may need to keep it on-premise in order to meet certain regulatory requirements.  Finally, it can help you meet performance requirements.  If you


### 2️⃣ Prompt: How do I run my models on-premise?

> \nHow do I run my models on-premise?\nI'm interested in running my models on-premise, but I'm not sure how to get started. Can you help?\nSure, I'd be happy to help! To run your models on-premise, you'll need to set up a server and install a machine learning framework like TensorFlow or PyTorch. You can then use the framework to train and deploy your models.\nHere are the general steps you'll need to follow:\n1. Choose a server: You'll need to choose

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \nRunning models on-premise can have several limitations, including:\n1. Security: Running models on-premise can be risky from a security perspective, as the data and models are stored on a local server, which can be vulnerable to cyberattacks.\n2. Scalability: Running models on-premise can be limited in terms of scalability, as the infrastructure needs to be built and maintained in-house, which can be time-consuming and expensive.\n3. Data privacy: Running models on-premise can also be a privacy concern, as the data is stored on a local server, which can be accessed by only a limited number of people.\n4. Maintenance: Running models on-premise can require a lot of maintenance, as the hardware and software need to be updated regularly to ensure optimal performance.\nOverall, running models on-premise can be a good option for organizations that have a small amount of data and models, but it may not be the best option for larger organizations with complex models and large amounts of data.#!/bin/bash\n# This script will install the latest version of TensorFlow on a Linux machine\n# It


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 \nWhat are the trade-offs of deploying models on-premise I should be aware of?\nI'm trying to decide whether to deploy a machine learning model on-premise or in the cloud. I'm aware of the benefits of on-premise deployment, such as greater control over the data and the model, and potentially lower costs if you have your own hardware. However, I'm also aware of the potential trade-offs, such as the need for specialized hardware and the potential for increased security risks.\nWhat are some other trade-offs I should be aware of?\nI'm also aware of the potential for increased maintenance and support costs if I deploy on-premise. Are there any other trade-offs I should be aware of?\nAdditionally, I'm aware of the potential for decreased flexibility if I deploy on-premise. Is this a significant concern for you, or would you rather have the control over the data and model?\nFinally, I'm aware of the potential for increased costs if I deploy on-premise. Are there any other costs I should be aware of?\nI'm trying to make an informed decision, so

</blockquote>

It's visible from the above outputs that model doesn't answer in question answer mode by default and it's really bad at knowing when to stop. We recommend users of `MPT 7B Chat` to develop guardrails and to take appropriate precautions for any production use as it's only behaves like a text generation model by default most of the time.

An example would be using a Chat Prompt Template as shown below:

Prompt:
```
You are an AI assistant in a conversational setting.
Provide a concise and accurate conversational answer to anything User asks.
===================

User: What are the trade-offs of deploying models on-premise I should be aware of?
Assistant:"""
```

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

chat = ChatOpenAI(openai_api_base="http://localhost:8450/v1", max_tokens=128)
messages = [HumanMessage(content="Why do I need to run machine learning models on-premise?")]
print(chat(messages))

# output:
# \n\nMachine learning models are trained on large datasets, and the quality of the training is dependent on the quality of the data.  If the data is stored on-premise, then the training process can take advantage of that.  If the data is stored in the cloud, then the training process must make do with whatever data is available in the cloud, which may not be the best quality.  Similarly, if the model is deployed on-premise, then it can take advantage of the on-premise data, but if it is deployed in the
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

chat = ChatOpenAI(openai_api_base="http://localhost:8450/v1", max_tokens=128)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

# output: > Finished chain.
# Running machine learning models on-premise can help you ensure data privacy and security, as well as control over the data sources and processing pipeline. It can also provide faster access to data and reduce latency, and enable you to customize your models and infrastructure to meet your specific needs.#

```

### 🔎 Quality Benchmarks


### 🚫 Limitations and Biases
We have noticed that the model doesn't fully behave like a question answering model by default, it's recommended to use this model with a Chat Prompt Template as shown above.

We recommend users of MPT-7B-Chat to develop guardrails and to take appropriate precautions while using it.


## 📜 License
MPT-7B-Chat can produce factually incorrect output, and should not be relied on to produce factually accurate information. MPT-7B-Chat was trained on various public datasets. While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.
It is made available under a license of CC-By-NC-SA-4.0 (for non-commercial use only)