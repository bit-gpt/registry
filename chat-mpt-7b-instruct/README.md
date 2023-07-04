# 📑 Documentation

## 📌 Description
MPT-7B-Instruct is a model for short-form instruction following. It is built by finetuning  <a href='https://huggingface.co/mosaicml/mpt-7b' target='_blank'>MPT-7B</a> on a <a href='https://huggingface.co/datasets/sam-mosaic/dolly_hhrlhf' target='_blank'>dataset</a> derived from the <a href='https://huggingface.co/datasets/databricks/databricks-dolly-15k' target='_blank'>Databricks Dolly-15k</a> and the  <a href='https://huggingface.co/datasets/Anthropic/hh-rlhf' target='_blank'>Anthropic Helpful and Harmless (HH-RLHF)</a> datasets.

## 💻 Hardware Requirements
To run the `mpt-7b-instruct` service on Prem, you'll need access to a GPU:

You'd need an A100, A10, or V100.

### A100 GPUs
A100 GPUs are preferred for training all model sizes.

### A10 GPUs

### V100 GPUs
It can be ran on V100 GPUs.

> **Memory requirements**: 14.1 GB (13455 MiB).


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \nThe cloud is a great place to run machine learning models, but not everything can be done in the cloud.\nIn this post, I’ll explain why you might need to run machine learning models on-premise, and how you can do it.\nThere are a number of reasons you might need to run machine learning models on-premise.\nThe first is security. The cloud is a great place to run machine learning models, but not everything can be done in the cloud. For example, you might have sensitive data that you don’t


### 2️⃣ Prompt: How do I run my models on-premise?

> \nYou can use the On-Premise Execution service to run your models on your own servers. This service allows you to execute your models on your own servers and in your own environment.\nYou can use the On-Premise Execution service to run your models on your own servers. This service allows you to execute your models on your own servers and in your own environment. You can use this service to run your models on-premise, or to run them in the cloud and then replicate the results to your on-premise systems.\nTo use the On

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \nThere are a few limitations to running your models on-premise.\nThe first limitation is the amount of data that can be processed. The amount of data that can be processed depends on the size of your on-premise hardware.\nThe second limitation is the time it takes to process the data. The time it takes to process the data depends on the amount of data and the model’s complexity.\nThe third limitation is the speed of your internet connection. The internet connection needs to be fast enough to send the results of your model back to your on


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

\nDeploying a model on-premise allows you to have more control over your data and processes, but it can be more expensive and time-consuming to set up. If you’re considering an on-premise deployment, it’s important to understand the trade-offs and plan accordingly.\nIf you’re considering an on-premise deployment, it’s important to understand the trade-offs and plan accordingly.The best way to learn how to use a new technology is to try it out.The best way to learn how to use a new technology is to try it out.\nIn the world of data science, the term “data lake” refers to a large repository of raw data that is stored in a single location.\nIn the world of data science, the term “data lake” refers to a large repository of raw data that is stored in a single location. Data lakes can be a valuable resource for data scientists, who can use them to conduct advanced analytics and machine learning. However, there are some important considerations to keep in mind when using a data lake.\nOne of the most important considerations is security. Data lakes

</blockquote>

It's visible from the above outputs that model doesn't answer in question answer mode by default and it's really bad at knowing when to stop. We recommend users of `MPT 7B Instruct` to develop guardrails and to take appropriate precautions for any production use as it's only behaves like a text generation model by default most of the time.

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

chat = ChatOpenAI(openai_api_base="http://localhost:8452/v1", max_tokens=128)
messages = [HumanMessage(content="Why do I need to run machine learning models on-premise?")]
print(chat(messages))

# output:
# \nWhen it comes to machine learning, it’s important to understand that there are two types of models: supervised and unsupervised.\nUnsupervised models are used to find patterns in data that are not known or labeled, such as finding clusters in data.\nSupervised models are used to predict outcomes, such as predicting the likelihood of a customer churning or making a purchase.\nTo train a supervised model, you need labeled data. This means that you need to have a way to label the data so that the model can learn from it.\nIn
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

chat = ChatOpenAI(openai_api_base="http://localhost:8452/v1", max_tokens=128)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

# output: > Finished chain.
# Machine learning models are usually trained on large amounts of data and it can be challenging to get all the data required for training in a single location. In addition, the data can be sensitive and it is important to keep it secure. Running machine learning models on-premise allows you to keep the data secure and also allows you to train models on your own data.\n#

```
---
##### This model was trained on data formatted in the dolly-15k format:

```python
INSTRUCTION_KEY = "### Instruction:"
RESPONSE_KEY = "### Response:"
INTRO_BLURB = "Below is an instruction that describes a task. Write a response that appropriately completes the request."
PROMPT_FOR_GENERATION_FORMAT = """{intro}
{instruction_key}
{instruction}
{response_key}
""".format(
    intro=INTRO_BLURB,
    instruction_key=INSTRUCTION_KEY,
    instruction="{instruction}",
    response_key=RESPONSE_KEY,
)

example = "James decides to run 3 sprints 3 times a week. He runs 60 meters each sprint. How many total meters does he run a week? Explain before answering."
fmt_ex = PROMPT_FOR_GENERATION_FORMAT.format(instruction=example)
# fmt_ex is ready to be tokenized and sent through the model.
```

### 🔎 Quality Benchmarks


### 🚫 Limitations and Biases
MPT-7B-Instruct can produce factually incorrect output, and should not be relied on to produce factually accurate information. MPT-7B-Instruct was trained on various public datasets. While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

We recommend users of MPT-7B-Instruct to develop guardrails, use it with above prompt templates and to take appropriate precautions while using it.


## 📜 License
It's released under CC-By-SA-3.0 which enables commercial usage with proper credits given.