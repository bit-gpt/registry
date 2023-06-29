# 📑 Documentation

## 📌 Description

Falcon-7B-Instruct is a 7B parameters causal decoder-only model built by TII based on Falcon-7B and finetuned on a mixture of chat/instruct datasets. The model is particularly designed for commercial use and its inference can be run on various GPU configurations. <a href='https://huggingface.co/tiiuae/falcon-7b-instruct' target='_blank'>Learn More</a>

## 💻 Hardware Requirements
To run the `falcon-7b-instruct` service on Prem, you'll need access to a GPU:

You'd need an A100, A10, or V100.

### A100 GPUs
A100 GPUs are preferred for training all model sizes.

### A10 GPUs

### V100 GPUs

> **Memory requirements**: 15.81 GB (15085 MiB).


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \nRunning machine learning models on-premise allows organizations to have more control over their data and computations. It also allows for the processing of large amounts of data in a high-performance environment, which can speed up the training and inference of models. Additionally, on-premise computing allows for integration with other applications and services.The main benefit of running a machine learning model on-premise is the ability to have more control over the data and computations, as well as the ability to process large amounts of data in a high-performance environment.


### 2️⃣ Prompt: How do I run my models on-premise?

> \nTo run models on-premise, you will need to ensure that your data and models are properly stored and secured. This can be done through various means, such as storing your data on your own cloud storage solution or using a public cloud platform. Additionally, you will need to ensure that you have appropriate permissions and access to your data and models. It is recommended to consult with your IT department or a data modeling expert to determine the best approach for running your models on-premise.The main problem that many companies face is the lack of scalability in their current infrastructure.

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \nThere are several limitations of running your models on-premise, such as hardware and software limitations, performance issues, network latency, security issues, and licensing costs. Additionally, running models on-premise may require significant infrastructure resources and maintenance, which can be costly.Powered by TradeKingThe best way to test a trading strategy is to use the demo environment provided by the trading platform.I also need to know how to set up the trading platform on my computer in order to use it for trading.\n- Can I use the trading platform on


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 \nDeploying models on-premise can offer several benefits, including improved latency, security, and data privacy. However, there are also trade-offs to consider, such as increased complexity, cost, and scalability. Additionally, on-premise models may require more resources for scaling and managing data, which can increase costs over time. It is important to weigh the costs and benefits of on-premise vs. cloud-based deployment to determine the best fit for your specific needs.I hope this helps!-EI\nWhat are some best practices for ensuring security when deploying models on-premise?\nAs models are deployed on-premise, it is important to ensure security measures to protect sensitive data and infrastructure. Some best practices include encrypting data transmissions, using role-based access controls, and implementing firewalls and intrusion detection systems. Additionally, regular security audits and evaluations should be conducted to ensure continued security measures. -EIThis is a great resource on best practices for deploying models on-premise. -EIThe following article offers a more in-depth guide to securing your on-premise deployment: 

</blockquote>

It's visible above from the outputs that model sometimes generates gibberish at the end and tends to hallucinate. We recommend users of Falcon-7B-Instruct to develop guardrails and to take appropriate precautions for any production use as it's only a text generation model by default.

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

chat = ChatOpenAI(openai_api_base="http://localhost:8448/v1", max_tokens=128)
messages = [HumanMessage(content="What are the trade-offs of deploying models on-premise I should be aware of?")]
print(chat(messages))
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

It outperforms comparable open-source models (e.g., MPT-7B, StableLM, RedPajama etc.)

Base model Falcon-7B is trained on English and French data only, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### 🚫 Limitations and Biases

We have noticed that the model sometimes generates responses that are not relevant and mostly gibberish like letters and numbers or just repeating the same words. E.g - xjskdafhnwne$. Also we found that it generates hashtag like words like #falcon7b, #falcon7binstruct etc, which seems to be a bias coming from the finetuning data as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

We recommend users of Falcon-7B-Instruct to develop guardrails and to take appropriate precautions for any production use.


## 📜 License
Falcon-7B was trained on 1,500B tokens of <a href='https://huggingface.co/datasets/tiiuae/falcon-refinedweb' target='_blank'>RefinedWeb</a>, a high-quality filtered and deduplicated web dataset which we enhanced with curated corpora. Significant components from our curated copora were inspired by <a href='https://arxiv.org/abs/2101.00027' target='_blank'>The Pile (Gao et al., 2020).</a>
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.