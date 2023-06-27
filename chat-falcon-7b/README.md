# 📑 Documentation

## 📌 Description

`falcon-7b`, developed by TII, is a 7B parameters causal decoder-only model trained on 1,500B tokens of RefinedWeb enhanced with curated corpora. The model is particularly designed for commercial use and its inference can be run on various GPU configurations. <a href='https://huggingface.co/tiiuae/falcon-7b' target='_blank'>Learn More</a>

## 💻 Hardware Requirements
To run the `falcon-7b` service on Prem, you'll need access to a GPU:

You'd need an A100, A10, or V100.

### A100 GPUs
A100 GPUs are preferred for training all model sizes.

### A10 GPUs

### V100 GPUs

> **Memory requirements**: 15.8 GB (15073 MiB).


## 📒 Example Usage

### 1️⃣ Prompt: Why do I need to run machine learning models on-premise?

> Running machine learning models on-premise allows you to control the computation, data, and metrics involved in the model lifecycle. This is important because the data and compute used to train a model can be quite large and typically cannot be shared across multiple organizations. Hosting the model on-premise also provides the flexibility to control access to the model and ensure the correct security requirements are met.


### 2️⃣ Prompt: How do I run my models on-premise?

> To run your models on-premise, you will first need to package them into a production-grade model deployment package (MDP). The MDP can be deployed on any cloud provider-compatible platform such as OpenAI Pet Store or AutoML packaging platform. For more information, see Model Deployment.

### 3️⃣ Prompt: What are the limitations of running my models on-premise?

> Some of the limitations you might run into are related to compliance, authentication and audit requirements. Depending on the regulations you are following you might be prevented from storing the model in the public cloud. Additionally, you might not be able to migrate the model to another provider or cloud because of non-standardized technologies or missing APIs.


### 4️⃣ Prompt: What are the trade-offs of deploying models on-premise I should be aware of?

<blockquote>

There are several considerations to take into account when deploying AI models in the enterprise. Depending on the deployment method, some of these considerations might not apply.

If the models are deployed as software as a service (SAAS) using an optimized cloud platform (e.g., using a dedicated hardware appliance, like Google Prediction API for Edge TPUs), the models deployment might not require any customization and the target platform should be properly dimensioned to sustain the expected workload.

If the models are deployed as a docker image, it should be properly built, optimized, and tuned for the target platform. In some cases, a cluster of machines with the right hardware and software configuration might be needed to sustain the expected workload.

If the models are deployed on-premise using a physical machine or a cluster, the models deployment might require customization, depending on the use case. The target platform should be properly dimensioned to sustain the expected workload.

In some cases, the models might require access to specific hardware or software components, which might not be available on the target platform.

In some other cases, the deployment method might be restricted by the agreements reached with the providers of the required hardware or software components.

</blockquote>


## 🛠️ Technical Details

### 🦜🔗 Getting Started with Langchain


```python
!pip install langchain
!pip install openai

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

Falcon-7B is trained on English and French data only, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

## 📜 License
Falcon-7B was trained on 1,500B tokens of <a href='https://huggingface.co/datasets/tiiuae/falcon-refinedweb' target='_blank'>RefinedWeb</a>, a high-quality filtered and deduplicated web dataset which we enhanced with curated corpora. Significant components from our curated copora were inspired by <a href='https://arxiv.org/abs/2101.00027' target='_blank'>The Pile (Gao et al., 2020).</a>
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.