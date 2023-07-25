# 📑 Documentation

## 📌 Description

Llama V2 7B, developed by Meta, is the 7B parameters version of auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety. It's released under a custom commercial license and its inference can be run on various GPU configurations. <a href='https://huggingface.co/meta-llama/Llama-2-7b' target='_blank'>Learn More</a>

## 💻 Hardware Requirements

> **Memory requirements**: 15.01 GB (14318 MiB).

To run the `llama-2-7b` service, you'll need the following hardware configuration:

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

> \nAnalyze your own data without any limits.\nMachine learning models are often very large, and may require high amounts of memory, disk space, and processing power.\nFor this reason, you\u2019ll need to run machine learning models on-premise, rather than in the cloud.\nIf you\u2019re working with a limited amount of data, you might be able to find a cloud-based solution that meets your needs.\nHowever, if you need to analyze data sets that are too large or too complex for a cloud-based solution


### 2️⃣ Prompt: How do I run my models on-premise?

> \nHow do I run my models on-premise?\nThe easiest way to run a model on-premise is to deploy a Docker containerized model and run it on your local machine or on a cloud machine.\nThis section only covers the basics. For a more detailed explanation, refer to our Docker-based Deployment Tutorial.\nDownload the Docker image of the model you\u2019d like to run on-premise from the Docker Hub.\nBuild a Docker container from the image:\ndocker build -t <your-unique-

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \nA. There are several different kinds of limitations.\nThe first is a limitation in the amount of data that can be processed. The typical cloud service runs on a shared computer, and the amount of data it can handle may be limited.\nThe second limitation is that the computer on which the model is running may not be secure. The computer may be exposed to hackers who can access the model and steal data.\nThe third limitation is that the computer on which the model is running may not be reliable. The computer may crash, or the model may


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 What should I be thinking about in terms of the IT infrastructure, security, and governance concerns? What are the ways to manage these concerns?\nWhat is the best way to run inference in the cloud for low-latency, high-precision models that are not suitable for on-premise deployment?\nWhat are the best ways to get started?\nHow can I manage the data costs?\nHow can I manage the costs of computing resources?\nHow can I manage the cost of deploying models

</blockquote>

It's visible above from the outputs that model sometimes tends to hallucinate or just does text completion. We recommend users of Llama-V2 7B to develop guardrails and to take appropriate precautions for any production use as it's only a text generation model by default.

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

chat = ChatOpenAI(openai_api_base="http://localhost:8227/v1", max_tokens=4096)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8227/v1", max_tokens=4096)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))
```

### 🚫 Limitations and Biases

Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide released by <a href='https://ai.meta.com/llama/responsible-use-guide/' target='_blank'>Meta here.</a>

## 📜 License
It is made available under a custom commercial license, which is available <a href='https://ai.meta.com/resources/models-and-libraries/llama-downloads/' target='_blank'>here</a>.