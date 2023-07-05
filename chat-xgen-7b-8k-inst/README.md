# 📑 Documentation

## 📌 Description

XGen-7B Instruct with 8k Context length is a 7B parameters model released by Salesforce, supervised fine tuned on public domain instructional data including databricks-dolly-15k, oasst1, Baize and GPT-related datasets. <a href='https://huggingface.co/Salesforce/xgen-7b-8k-inst' target='_blank'>Learn More</a> and <a href='https://blog.salesforceairesearch.com/xgen/#note-on-potential-risks' target='_blank'>Blog here</a>.

## 💻 Hardware Requirements

> **Memory requirements**: 15.79 GB (15065 MiB).

To run the `xgen-7b-8k-inst` service, you'll need the following hardware configuration:

#### Cloud Platforms

If you are using AWS:

- Instance Type: `p3.2xlarge` or higher
- GPU: NVIDIA V100 or higher.

If you are using Paperspace:

- Instance Type: `V100` or higher
- GPU: NVIDIA V100 or higher.

#### On-Premise Platforms

You'll need access to a GPU with the following options:

- V100 GPUs: The model can be run on V100 GPUs.


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> \nThe first reason is that some organizations have compliance and regulatory requirements that mandate the use of on-premise infrastructure. For example, some industries, such as healthcare and finance, have strict regulations that require data to be stored and processed within their own premises.\n\nThe second reason is that some organizations want to have full control over their data and infrastructure. By running machine learning models on-premise, organizations can ensure that they have full visibility and control over their data and models, and can prevent data breaches or other security incidents.\n\nThe third reason is


### 2️⃣ Prompt: How do I run my models on-premise?

> \nI am interested in using on-premise solutions for my machine learning models. How do I run my models on-premise?\nThis article has been viewed 53,872 times.\nIf you have a big project to start, or simply need to feel more organized, there are several strategies you can use to stay on top of your tasks and achieve a sense of calm and focus. Here are some effective ways to increase your productivity and reduce distractions while working on a computer.\nUse a headset or other noise-canceling headphones. These will reduce backgrou

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> \n### Assistant: There are several limitations to running models on-premise, including:\n\n1. Limited scalability: Running models on-premise can be limited in terms of scalability. If your model needs to handle a large number of users or data, it may not be able to do so efficiently.\n2. Limited access to resources: On-premise models may not have access to the same resources as cloud-based models, such as high-performance computing (HPC) resources or advanced data analytics tools.\n3. Limited flexibility:


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

 \n### Assistant: When deploying machine learning models on-premise, there are several trade-offs to consider. Some of the key factors to think about include:\n\n1. Data security and privacy: When data is stored on-premise, it is physically stored in a location that is under the control of the organization. This can be beneficial in terms of data security and privacy, as the organization has full control over the data and can implement additional security measures to protect it. However, it also means that the organization is responsible for the physical security of the data and any breaches could have serious consequences.\n2. Scalability: On-premise deployment can be more difficult to scale than cloud-based deployment, as the organization is responsible for purchasing and maintaining the necessary hardware and infrastructure. This can be a significant investment and may limit the organization's ability to quickly scale up or down as needed.\n3. Maintenance and support: When deploying models on-premise, the organization is responsible for maintaining and supporting the hardware and infrastructure. This can be time-consuming and expensive, as the organization may need to hire additional staff or contractors to manage the infrastructure.\n

</blockquote>

It's visible above from the outputs that model sometimes generates gibberish and tends to hallucinate if prompted without any special techniques. We recommend users of XGen models to develop guardrails and to take appropriate precautions for any production use as it's only at auto-regressive text generation by default.

An example would be using a Chat Prompt Template as shown below to improve performance:

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

chat = ChatOpenAI(openai_api_base="http://localhost:8449/v1", max_tokens=128)
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

chat = ChatOpenAI(openai_api_base="http://localhost:8449/v1", max_tokens=128)
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))
```

### 🔎 Quality Benchmarks

On standard NLP benchmarks, XGen achieves comparable or better results when compared with state-of-the-art open-source LLMs (e.g. MPT, Falcon, LLaMA, Redpajama, OpenLLaMA) of similar model size.
Our targeted evaluation on long sequence modeling benchmarks show benefits of our 8K-seq models over 2K- and 4K-seq models.

XGen-7B achieves equally strong results both in text (e.g., MMLU, QA) and code (HumanEval) tasks.

We have tested both xgen-7b-8k-inst and xgen-7b-8k-base models on similar set of questions and in results we found xgen-7b-8k-inst model to be more accurate in generating better responses. Results can be found [here](https://github.com/premAI-io/prem-registry/tree/dev/chat-xgen-7b-8k-inst/results).

### 🚫 Limitations and Biases

We have noticed that the model sometimes generates responses that are totally irrelevant and mostly gibberish like some random code, etc. Using a Chat Prompt Template as shown above can help improve performance.
We recommend users of XGen models to develop guardrails and to take appropriate precautions for any production use.

The creators of XGen 7B have mentioned that despite their effort in addressing the risks of bias, toxicity and hallucinations both in pre-training and fine-tuning stages, like other LLMs, XGen-7b models are not free from such limitations. We hope our open-sourced codebase will help other researchers better understand these challenges and improve on these key limitations for making AI beneficial for everyone.


## 📜 License
It's only mentioned to use for research purposes. Refer to the repo <a href='https://github.com/salesforce/xgen#models' target='_blank'>here</a>.