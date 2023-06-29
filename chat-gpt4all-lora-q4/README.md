# 📑 Documentation

## 📌 Description

GPT4All, developed by Nomic AI, is a chatbot trained over an extensive corpus of assistant interactions. By finetuning LLaMA 7B, GPT4All provides an open-source ecosystem to train and deploy efficient, assistant-style large language models locally on consumer-grade CPUs. This democratized approach to AI aims to bolster open research, reproducibility, and promote developments in AI alignment and interpretability. The current model has been 4-bit quantized using ggml framework. [Learn more](https://github.com/nomic-ai/gpt4all).

## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> There are several reasons why you might want to run machine learning models on-premise. One reason is that it can provide greater control over the data and model, which can be important for certain use cases. Another reason is that it can allow for faster execution times, as there may not be a need to wait for cloud infrastructure or resources. Additionally, some organizations may have regulatory requirements that require them to keep sensitive data on-premise rather than in the cloud.

### 2️⃣ Prompt: How do I run my models on-premise?

> You can run your models on-premise by installing the necessary software and hardware requirements. You will need to have a server or a cluster of servers with sufficient processing power, memory, storage space, and network bandwidth to handle the computational load of your model. You may also require specialized hardware, such as GPUs, for accelerated computing. Once you have all the required resources, you can install the necessary software packages and configure them according to your needs.

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> There are several limitations when running models on-premise, such as high upfront costs for hardware and software, limited scalability due to physical constraints, and a lack of flexibility in terms of deployment options. Additionally, maintaining and upgrading the infrastructure can be time-consuming and costly.

### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

> There are several trade-offs to consider when deploying models on-premise, such as increased costs, limited scalability, and a lack of flexibility in terms of deployment options. Additionally, maintaining and upgrading the infrastructure can be time-consuming and costly.


## 🛠️ Technical Details

### 🔧 Training / Fine Tuning Costs

> After a significant effort spanning four days and a substantial expenditure of $800 for GPU rentals from providers such as Lambda Labs and Paperspace, the resulting model, named gpt4all-lora, is now up and running. This sum includes the costs incurred from several unsuccessful training attempts. In addition to the GPU costs, a further $500 was expended on the OpenAI API. 

However, the training duration has been drastically reduced with the model's release. Now, the entire training process can be completed in approximately eight hours using Lambda Labs' DGX A100 8x 80GB setup, at a significantly reduced total cost of $100.

### 🔢 Default Parameters

For our experiments, we have been using the following parameters:

```python
temperature=0.2
top_p=0.95
stop=[]
max_tokens=256
repeat_penalty=1.1
```

### 🔎 Quality Benchmarks

For more information about GPT4All performances and quality, you can visit: https://gpt4all.io/index.html.

### 🚀 Serving Details

To expose the service, we currently use FastAPI and [llama-cpp-python](https://abetlen.github.io/llama-cpp-python/) library which is compatible with all ggml models.

```python
llama-cpp-python==0.1.43
```

### ⚪️ Embeddings

The current model supports embedding generation too. Another endpoint is exposed for this purpose. You can check out the documentation for each container to see how to use it at `http://{container_ip}:8000/docs` or at our public services [Open API documentation](https://mock.prem.ninja/docs).

### 🦜🔗 Getting Started (using LangChain)

```python
!pip install langchain
!pip install openai

import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

os.environ["OPENAI_API_KEY"] = "random-string"

chat = ChatOpenAI(openai_api_base="http://localhost:8222/v1", max_tokens=128)

messages = 
    HumanMessage(content="Why do I need to run machine learning models on-premise?")
]

chat(messages)
```

### Speeding Up Inference

By default, the model uses (1/2 + 1) the number of cores available on the underlying hardware. If you want to use more cores, you can pass an arbitrary number to the request parameter `n_threads`. Theoretically, this method will improve inference time.

```json
{
  "model": "string",
  "messages": [
    {}
  ],
  "temperature": 0.2,
  "top_p": 0.95,
  "n": 1,
  "stream": false,
  "stop": [],
  "max_tokens": 256,
  "presence_penalty": 0,
  "frequence_penalty": 0,
  "logit_bias": {},
  "user": "",
  "n_threads": 0 // this is the parameter required to change in order use more cpu cores.
}
```

## 📜 License

The model is a research preview intended for **non-commercial use only**, subject to the model License of LLaMA, Terms of Use of the data generated by OpenAI.
