# 📑 Documentation

## 📌 Description

Llama V2 13B Chat, developed by Meta, is an auto-regressive language model that uses an optimized transformer architecture. It's a 13B parameters finetuned Chat model version using supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety. It's released under a custom commercial license and its inference can be run on various GPU configurations. <a href='https://huggingface.co/meta-llama/Llama-2-13b-chat' target='_blank'>Learn More</a>

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

> To know more on how to handle multi-turn conversation prompts specially for Llama-v2, check out: https://huggingface.co/blog/llama2#how-to-prompt-llama-2


### 🚫 Limitations and Biases

Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide released by <a href='https://ai.meta.com/llama/responsible-use-guide/' target='_blank'>Meta here.</a>

## 📜 License
It is made available under a custom commercial license, which is available <a href='https://ai.meta.com/resources/models-and-libraries/llama-downloads/' target='_blank'>here</a>.