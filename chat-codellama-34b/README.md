# 📑 Documentation

## 📌 Description

Code Llama is a series of pretrained generative text models developed by Meta, designed for code synthesis and understanding. These models come in three sizes (7B, 13B, 34B parameters) and have three variants: a base model, a Python-specific version, and an Instruct version for instruction following. They are intended for commercial and research applications, specifically in English and programming languages. The models have been trained using Meta's Research Super Cluster, with the training process having a carbon footprint of 65.3 tCO2eq, fully offset by Meta's sustainability program. Due to the novelty and unpredictability of the technology, users are advised to exercise caution, especially in deployment, and to refer to the Responsible Use Guide provided by Meta. [Learn More](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf)

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

chat = ChatOpenAI(openai_api_base="http://localhost:8453/v1", max_tokens=1024)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8453/v1", max_tokens=1024)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

# output: > Finished chain.
# Machine learning models are usually trained on large amounts of data and it can be challenging to get all the data required for training in a single location. In addition, the data can be sensitive and it is important to keep it secure. Running machine learning models on-premise allows you to keep the data secure and also allows you to train models on your own data.\n#

```

### 🔎 Quality Benchmarks

### 🚫 Limitations and Biases

Code Llama and its variants are a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Code Llama’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate or objectionable responses to user prompts. Therefore, before deploying any applications of Code Llama, developers should perform safety testing and tuning tailored to their specific applications of the model.

## 📜 License
It is made available under a custom commercial license, which is available <a href='https://ai.meta.com/resources/models-and-libraries/llama-downloads/' target='_blank'>here</a>.