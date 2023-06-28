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

> **Memory requirements**: 15.4 GB (14705 MiB).


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> Running machine learning models on-premise allows you to maintain control over the environment and data, ensuring that the models can execute at scale with data autonomy. It's also cost-efficient in the long-run as it eliminates the need for data lake replication or cloud-based storage costs. Additionally, it reduces the latency that can be associated with accessing data from the internet or cloud. Running machine learning models on-premise also improves data security by keeping your data confidential and protected.


### 2️⃣ Prompt: How do I run my models on-premise?

> To run your models on-premise, you will need to have a suitable hardware and software setup. It depends on the type of models you want to run, but typically you will need a powerful processor and sufficient memory. You will need to install and configure a data-processing software, such as Apache Hadoop or Spark, and you will also need to install a database software to store and process data. Once you have everything set up, you can train your models and run them on your on-premise hardware for faster processing

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> Running your models on-premise has its limitations. On-premise solutions provide you with the highest level of control over your data and infrastructure, but they also come with higher costs and limited scalability. Additionally, on-premise solutions require more maintenance and upkeep, and may not be as flexible or adaptable as cloud-based solutions. In the end, the decision depends on factors like your budget, data needs, and desired level of control.The best is to consider using a combination of on-premise and cloud-based solutions to get the best of both worlds.


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 Deploying models on-premise can be both beneficial and challenging. Some of the advantages of deploying your models on-premise include centralized management and security, access to more powerful hardware and processing resources, and improved performance.
 
 In contrast, there are some trade-offs to consider. Deploying on-premise can be costly in terms of equipment, maintenance, and updates. Additionally, it can be difficult to scale the models as the number of users increases. On the other hand, deploying models on-premise can provide increased control and privacy, as well as improved compliance with data and security regulations.
 
 It is important to consider the specific needs and goals of your organization before deciding whether to deploy models on-premise or not

</blockquote>


## 🛠️ Technical Details

### 🦜🔗 Getting Started with Langchain

For using falcon-7b-instruct in a chat setting we recommend using a Chat Prompt Template as shown below, same template was used to generate responses for the above examples.:

```bash
pip install langchain openai
```
    
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