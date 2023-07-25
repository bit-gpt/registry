# 📑 Documentation

## 📌 Description

Falcon-7B-Instruct is a 7B parameters causal decoder-only model built by TII based on Falcon-7B and finetuned on a mixture of chat/instruct datasets. The model is particularly designed for commercial use and its inference can be run on various GPU configurations. <a href='https://huggingface.co/tiiuae/falcon-7b-instruct' target='_blank'>Learn More</a>

## 💻 Hardware Requirements

> **Memory requirements**: 27.69 GB (26406 MiB).

To run the `llama-2-13b-chat` service, you'll need the following hardware configuration:

### Cloud Platforms

If you are using AWS:

- Instance Type: `p3.2xlarge` or higher
- GPU: NVIDIA A100, NVIDIA V100 (2x)

If you are using Paperspace:

- Instance Type: `V100-32G` or `A100` or higher
- GPU: NVIDIA A100, NVIDIA V100

### On-Premise Platforms

You'll need access to a GPU with the following options:
- A100 GPUs: A100 GPUs are preferred for training all model sizes, and are the only GPUs that can train the 13B param model in a reasonable amount of time.
- A10 GPUs: Training the 13B param model is not recommended on A10s.

## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \n\nThere are several reasons why you might want to run machine learning models on-premise, rather than in the cloud:\n\n1. Data privacy and security: If you are working with sensitive data, you may not want to transmit it to the cloud for processing. By running your models on-premise, you can keep your data within your own network and maintain greater control over its security.\n2. Performance: Depending on the size and complexity of your data, you may find that running your models on-premise is


### 2️⃣ Prompt: How do I run my models on-premise?

> \n\nYou can run your machine learning models on-premise using a variety of methods, depending on your specific needs and requirements. Here are some general strategies you can consider:\n\n1. Install the necessary software and libraries: You will need to install the necessary software and libraries for your machine learning models on your on-premise environment. This may include popular machine learning frameworks like scikit-learn, TensorFlow, or PyTorch, as well as other dependencies like Python or R.\n2. Use a containerization platform: Containerization

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \n\nThe limitations of running your machine learning models on-premise include:\n\n1. Compute and storage constraints: You may have limited compute and storage resources on-premise, which can limit the size and complexity of the models you can train.\n2. Maintenance and upgrades: On-premise infrastructure requires regular maintenance and upgrades, which can be time-consuming and may disrupt your model training and deployment.\n3. Security and compliance: On-premise infrastructure may


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 \n\nThere are several trade-offs to consider when deploying machine learning models on-premise, including:\n\n1. Cost: On-premise deployment can be more expensive than cloud-based deployment, as it requires investment in hardware, software, and maintenance.\n2. Security: On-premise deployment can provide better security and control over data, but it also requires additional security measures to protect against unauthorized access and data breaches.\n3. Scalability: On

</blockquote>

We recommend users of Llama-V2-13B-Chat to develop guardrails and to take appropriate precautions for any production use as it's only a text generation model by default, tuned to give responses in a QnA setting.

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

chat = ChatOpenAI(openai_api_base="http://localhost:8230/v1", max_tokens=4096)
messages = [HumanMessage(content="What are the trade-offs of deploying models on-premise I should be aware of?")]
print(chat(messages))
```

For using it in a chat setting we recommend using a Chat Prompt Template as shown below:

> To know more on how to handle multi-turn conversation prompts specially for Llama-v2, check out: https://huggingface.co/blog/llama2#how-to-prompt-llama-2
    
```python

import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "random-string"

chat_template = """<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

{user_message} [/INST]"""

prompt = PromptTemplate(
    input_variables=["user_message"],
    template=chat_template,
)

user_message = "Why do I need to run machine learning models on-premise?"

chat = ChatOpenAI(openai_api_base="http://localhost:8230/v1", max_tokens=4096)
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