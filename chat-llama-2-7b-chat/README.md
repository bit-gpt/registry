# 📑 Documentation

## 📌 Description

Falcon-7B-Instruct is a 7B parameters causal decoder-only model built by TII based on Falcon-7B and finetuned on a mixture of chat/instruct datasets. The model is particularly designed for commercial use and its inference can be run on various GPU configurations. <a href='https://huggingface.co/tiiuae/falcon-7b-instruct' target='_blank'>Learn More</a>

## 💻 Hardware Requirements

> **Memory requirements**: 15.01 GB (14318 MiB).

To run the `llama-2-7b-chat` service, you'll need the following hardware configuration:

### Cloud Platforms

If you are using AWS:

- Instance Type: `p3.2xlarge` or higher
- GPU: NVIDIA A100, NVIDIA V100

If you are using Paperspace:

- Instance Type: `V100` or higher
- GPU: NVIDIA A100, NVIDIA V100

### On-Premise Platforms

You'll need access to a GPU with the following options:
- A100 GPUs: A100 GPUs are preferred for training all model sizes.
- V100 GPUs: The model can be run on V100 GPUs.

## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \n\nMachine learning models are typically trained on large datasets that are too large or too sensitive to be stored or transmitted securely over the internet. Running machine learning models on-premise allows you to keep your data local and avoid any potential security risks associated with transmitting sensitive data over the internet. Additionally, running machine learning models on-premise can provide better performance and faster training times, as you don't have to rely on internet connectivity.\n\n\nsources:\n\n1. \"Why Run Machine Learning Mod


### 2️⃣ Prompt: How do I run my models on-premise?

> \n\nI have a few models that I have trained using TensorFlow and PyTorch, and I would like to run them on-premise, without using any cloud services. How can I do this?\n\nOption 1: Install TensorFlow and PyTorch on your local machine\n\nTo run your models on-premise, you can install TensorFlow and PyTorch on your local machine. Here are the steps for installing TensorFlow and PyTorch on a Windows, macOS, or Linux machine:\n\n

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \n\nAnswer: Running machine learning models on-premise has several limitations, including:\n\n1. Data Security: By running your models on-premise, you may be exposing your data to potential security threats, such as data breaches or cyber attacks.\n2. Limited Scalability: On-premise models may not be able to handle large datasets or high volumes of traffic, which can limit their scalability.\n3. Difficulty in Managing Model Updates: Keeping your models up


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 \n\nThere are several trade-offs to consider when deciding whether to deploy machine learning models on-premise or in the cloud:\n\n1. Control and Security: On-premise deployment provides greater control over the underlying infrastructure, which can be critical for sensitive or regulated industries. However, this control comes at the cost of increased security and maintenance responsibilities.\n2. Cost: Deploying models on-premise can require significant upfront costs for hardware and infrastructure,

</blockquote>

It's visible above from the outputs that model sometimes tends just do text completion and not respond in a QnA manner. We recommend users of Llama-V2-7B-Chat to develop guardrails and to take appropriate precautions for any production use as it's only a text generation model by default.

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

chat = ChatOpenAI(openai_api_base="http://localhost:8228/v1", max_tokens=4096)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8228/v1", max_tokens=4096)
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