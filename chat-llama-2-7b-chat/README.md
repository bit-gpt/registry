# 📑 Documentation

## 📌 Description

Llama V2 7B Chat, developed by Meta, is an auto-regressive language model that uses an optimized transformer architecture. It's a 7B parameters finetuned Chat model version using supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety. It's released under a custom commercial license and its inference can be run on various GPU configurations. <a href='https://huggingface.co/meta-llama/Llama-2-7b-chat' target='_blank'>Learn More</a>

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

### 🚫 Limitations and Biases

Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide released by <a href='https://ai.meta.com/llama/responsible-use-guide/' target='_blank'>Meta here.</a>

## 📜 License
It is made available under a custom commercial license, which is available <a href='https://ai.meta.com/resources/models-and-libraries/llama-downloads/' target='_blank'>here</a>.