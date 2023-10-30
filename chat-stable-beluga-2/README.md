# 📑 Documentation

## 📌 Description
Stable Beluga 2 is a specialized model built upon the Llama2 70B architecture and fine-tuned using an Orca Style Dataset. This model is available for free testing through Stable Chat's Research Preview platform, aimed at showcasing Stability AI's most advanced language models.

## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> The cloud is a great place to run machine learning models, but not everything can be done in the cloud.
> In this post, I’ll explain why you might need to run machine learning models on-premise, and how you can do it.
> There are a number of reasons you might need to run machine learning models on-premise.
> The first is security. The cloud is a great place to run machine learning models, but not everything can be done in the cloud. For example, you might have sensitive data that you don’t


### 2️⃣ Prompt: How do I run my models on-premise?

> You can use the On-Premise Execution service to run your models on your own servers. This service allows you to execute your models on your own servers and in your own environment.
> You can use the On-Premise Execution service to run your models on your own servers. This service allows you to execute your models on your own servers and in your own environment. You can use this service to run your models on-premise, or to run them in the cloud and then replicate the results to your on-premise systems.
> To use the On

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> There are a few limitations to running your models on-premise.
> The first limitation is the amount of data that can be processed. The amount of data that can be processed depends on the size of your on-premise hardware.
> The second limitation is the time it takes to process the data. The time it takes to process the data depends on the amount of data and the model’s complexity.
> The third limitation is the speed of your internet connection. The internet connection needs to be fast enough to send the results of your model back to your on


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

> Deploying a model on-premise allows you to have more control over your data and processes, but it can be more expensive and time-consuming to set up. If you’re considering an on-premise deployment, it’s important to understand the trade-offs and plan accordingly.
> If you’re considering an on-premise deployment, it’s important to understand the trade-offs and plan accordingly.The best way to learn how to use a new technology is to try it out.The best way to learn how to use a new technology is to try it out.
> In the world of data science, the term “data lake” refers to a large repository of raw data that is stored in a single location.
> In the world of data science, the term “data lake” refers to a large repository of raw data that is stored in a single location. Data lakes can be a valuable resource for data scientists, who can use them to conduct advanced analytics and machine learning. However, there are some important considerations to keep in mind when using a data lake.
> One of the most important considerations is security. Data lakes


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

chat = ChatOpenAI(openai_api_base="http://localhost:8734/v1", max_tokens=512)
messages = [HumanMessage(content="Why do I need to run machine learning models on-premise?")]
print(chat(messages))

# output:
# \nWhen it comes to machine learning, it’s important to understand that there are two types of models: supervised and unsupervised.\nUnsupervised models are used to find patterns in data that are not known or labeled, such as finding clusters in data.\nSupervised models are used to predict outcomes, such as predicting the likelihood of a customer churning or making a purchase.\nTo train a supervised model, you need labeled data. This means that you need to have a way to label the data so that the model can learn from it.\nIn
```

### 🔎 Quality Benchmarks

### 🚫 Limitations and Biases

Beluga is an emerging technology with inherent risks. Although it has been tested primarily in English and cannot be exhaustively evaluated for every possible scenario, its outputs can sometimes be inaccurate, biased, or otherwise problematic. Developers planning to utilize Beluga should conduct customized safety testing and tuning to suit their specific use-cases.

## 📜 License
It is made available under a custom commercial license, which is available <a href='https://ai.meta.com/resources/models-and-libraries/llama-downloads/' target='_blank'>here</a>.