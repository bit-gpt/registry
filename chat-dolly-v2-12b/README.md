# 📑 Documentation

## 📌 Description

`dolly-v2-12b`, developed by Databricks, is an instruction-following large language model trained on diverse capability domains. It exhibits remarkable instruction following behavior, surpassing the foundation model it's based on, Pythia-12b. The model is particularly designed for commercial use and its inference can be run on various GPU configurations. <a href='https://huggingface.co/databricks/dolly-v2-12b' target='_blank'>Learn More</a>

## 💻 Hardware Requirements

> **Memory requirements**: 23.91GiB GB (24484 MiB).

To run the `dolly-v2-12b` service, you'll need the following hardware configuration:

### Cloud Platforms

If you are using AWS:

- Instance Type: `p3.2xlarge` or higher
- GPU: NVIDIA A100, NVIDIA V100
  - When using V100s (e.g., `p3.2xlarge`, 1 x V100 16GB)  set `torch_dtype=torch.float16` in `pipeline()` instead. The 12B param model may not function well in 8-bit.

If you are using Paperspace:

- Instance Type: `V100-32G` or `A100` or higher
- GPU: NVIDIA A100, NVIDIA V100

### On-Premise Platforms

You'll need access to a GPU with the following options:
- A100 GPUs: A100 GPUs are preferred for training all model sizes, and are the only GPUs that can train the 12B param model in a reasonable amount of time.
- A10 GPUs: Training the 12B param model is not recommended on A10s.
- V100 GPUs: When using V100s (e.g., `p3.2xlarge`, 1 x V100 16GB, `NC6s_v3`), in all cases, set `torch_dtype=torch.float16` in `pipeline()` instead. The 12B param model may not function well in 8-bit.


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
from langchain.schema import AIMessage, HumanMessage

os.environ["OPENAI_API_KEY"] = "random-string"

chat = ChatOpenAI(openai_api_base="http://localhost:8333/v1", max_tokens=128)

messages = 
    HumanMessage(content="Why do I need to run machine learning models on-premise?")

chat(messages)
```

### 🔎 Quality Benchmarks

According to the known limitations, `dolly-v2-12b` is not state of the art. It is not designed to out-perform more mordern architectures and in fact underperforms `dolly-v1-6b` in some evaluation benchmarks.

Check out the <a href='https://github.com/databrickslabs/dolly#known-limitations' target='_blank'>other limitations</a>.

## 📜 License

`dolly-v2-12b` is a 12 billion parameter causal language model created by <a href='https://databricks.com/' target='_blank'>Databricks</a> that is derived from <a href='https://www.eleuther.ai/' target='_blank'>EleutherAI</a>’s <a href='https://huggingface.co/EleutherAI/pythia-12b' target='_blank'>Pythia-12b</a> and fine-tuned on a <a href='https://github.com/databrickslabs/dolly/tree/master/data' target='_blank'>~15K record instruction corpus</a> generated by Databricks employees and released under a permissive license (CC-BY-SA).