# 📑 Documentation

## 📌 Description
MPT-7B is a decoder-style transformer pretrained from scratch on 1T tokens of English text and code. This model was trained by <a href='https://www.mosaicml.com/' target='_blank'>MosaicML</a>.

MPT-7B is part of the family of MosaicPretrainedTransformer (MPT) models, which use a modified transformer architecture optimized for efficient training and inference.



## 💻 Hardware Requirements
> **Memory requirements**: 14.1 GB (13455 MiB).

To run the `mpt-7b` service, you'll need the following hardware configuration:

### Cloud Platforms

If you are using AWS:

- Instance Type: `p3.2xlarge` or higher
- GPU: NVIDIA V100 or higher.

If you are using Paperspace:

- Instance Type: `V100` or higher
- GPU: NVIDIA V100 or higher.

### On-Premise Platforms

You'll need access to a GPU with the following options:

- V100 GPUs: The model can be run on V100 GPUs.


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \nWhen it comes to running machine learning models, you have two options: run them on-premise or run them in the cloud.\nOn-premise means that you are running the machine learning models on your own servers. This is typically done by an organization that wants to keep their data and models in-house, or because they don’t have the resources to run the models in the cloud.\nRunning machine learning models on-premise can be a great option if you have the resources to do so. It allows you to have complete control over


### 2️⃣ Prompt: How do I run my models on-premise?

> \nThe on-premise option is available for those customers who want to run their models on their own hardware. The on-premise option is available for all models except the Financial Services models.\nHow do I run my models in the cloud?\nThe cloud option is available for those customers who want to run their models on a secure, hosted environment. The cloud option is available for all models except the Financial Services models.\nWhat is the difference between the cloud and on-premise options?\nThe cloud option is a hosted environment where the model is run on a

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \nOn-premise software can be expensive and require a lot of maintenance. You also have to pay for the hardware, and if you want to add new features or fix bugs, you have to wait for the vendor to release a new version.\nWith a cloud-based model management solution, you can access your models from anywhere, anytime, and on any device. You can also update your models in real-time and add new features without waiting for a new release.\nWith a cloud-based model management solution, you can access your models from anywhere, anytime


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 \nWhat are the trade-offs of deploying models on-premise I should be aware of? How can I minimize the risks of deploying models on-premise?\nThe first thing to consider is the level of control you have over the environment in which the model is deployed. If you are deploying the model on-premise, you have complete control over the environment. You can ensure that the model is deployed in a secure environment and that the environment is properly maintained. You can also ensure that the model is deployed in an environment that meets the performance requirements of the model.\nThe second thing to consider is the level of control you have over the data that the model is using. If you are deploying the model on-premise, you have complete control over the data that the model is using. You can ensure that the data is accurate and up-to-date. You can also ensure that the data is protected from unauthorized access.\nThe third thing to consider is the level of control you have over the users of the model. If you are deploying the model on-premise, you have complete control over the users of the model. You can ensure that

</blockquote>

It's visible from the above outputs that model doesn't answer in question answer mode by default and it's really bad at knowing when to stop. We recommend users of `MPT 7B` to develop guardrails and to take appropriate precautions for any production use as it's only behaves like a text generation model by default most of the time.

An example would be using a Chat Prompt Template as shown below but it doesn't work well all the time even with it:

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

chat = ChatOpenAI(openai_api_base="http://localhost:8451/v1", max_tokens=128)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8451/v1", max_tokens=128)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

# output: > Finished chain.
# Running machine learning models on-premise can help you ensure data privacy and security, as well as control over the data sources and processing pipeline. It can also provide faster access to data and reduce latency, and enable you to customize your models and infrastructure to meet your specific needs.#

```

### 🔎 Quality Benchmarks


### 🚫 Limitations and Biases
MPT-7B (Base) is not intended for deployment without finetuning. It should not be used for human-facing interactions without further guardrails and user consent.

MPT-7B can produce factually incorrect output, and should not be relied on to produce factually accurate information. MPT-7B was trained on various public datasets. While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.


## 📜 License
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.