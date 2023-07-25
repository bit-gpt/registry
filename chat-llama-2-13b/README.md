# 📑 Documentation

## 📌 Description

Falcon-7B-Instruct is a 7B parameters causal decoder-only model built by TII based on Falcon-7B and finetuned on a mixture of chat/instruct datasets. The model is particularly designed for commercial use and its inference can be run on various GPU configurations. <a href='https://huggingface.co/tiiuae/falcon-7b-instruct' target='_blank'>Learn More</a>

## 💻 Hardware Requirements

> **Memory requirements**: 27.69 GB (26406 MiB).

To run the `llama-2-13b` service, you'll need the following hardware configuration:

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

> \nThe model runs on-premise, but the data runs in the cloud. The model is trained in the cloud, but the data is stored on-premise. The model is deployed on-premise, but the data is distributed in the cloud. The data is stored in the cloud, but the model is trained on-premise. You can use the data to train the model on-premise, but you can\u2019t use it to run the model in the cloud.\nWhy do I need to run machine


### 2️⃣ Prompt: How do I run my models on-premise?

> \\n\nI have been trained a model in Azure ML. I want to run it on-premise.\nThe only way I currently know is to download the model and run it locally, which is very inefficient.\nIs there a way to run the model on-premise without downloading it?\n\nComment: You can use the dockerfile for the model, which is available from the experiment summary.\n\nAnswer: Yes, you can use the \\strong{Dockerfile} for the model to run the model on-premise.

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \\nThe on-premise solution can be deployed in a private or public cloud. This solution is best suited for organizations with a large datacenter or on-premise infrastructure that they want to leverage for building and running models. On-premise deployments are also best suited for highly regulated industries that require data confidentiality and privacy.\nIs the on-premise solution based on a software-as-a-service (SaaS) model?\nNo. It is based on a software


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

**Response 1:**
<blockquote>

\n\nComment: @snowman1391: I'm not sure I understand the trade-off question.  Is it about the performance of the models running on-premise vs. in the cloud?\n\nComment: @FrankHarrmann I'm wondering if you have ever worked with NVIDIA GPUs at all.  I'm specifically asking about the trade-offs of GPUs vs. CPUs, and I'm wondering if it's worth it for my

</blockquote>

**Response 2:**
<blockquote>
\n\nComment: @Anirudh I'm only aware of [this](https://github.com/tensorflow/models/issues/220) and [this](https://github.com/tensorflow/models/issues/3131) issue. I'm not aware of any issues in particular with the model's performance. Are you aware of any?\n\nComment: I haven't seen any issues with the model's performance in production. However, I believe it's
</blockquote>


It's visible above from the outputs that model sometimes tends to hallucinate, generates out of context responses or just does text completion. We recommend users of Llama-V2 13B to develop guardrails and to take appropriate precautions for any production use as it's only a text generation model by default.

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

chat = ChatOpenAI(openai_api_base="http://localhost:8229/v1", max_tokens=4096)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8229/v1", max_tokens=4096)
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