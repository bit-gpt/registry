# 📑 Documentation

## 📌 Description

CodeGen-Multi 2B is part of the CodeGen family, specifically designed for program synthesis in languages like C, C++, Go, Java, JavaScript, and Python. Initialized with CodeGen-NL 2B, it was further pre-trained on BigQuery with 119.2B tokens, utilizing cross-entropy loss and multiple TPU-v4-512 by Google. Best suited for generating executable code from English prompts, it can also complete partially-generated code. Loading and utilization are facilitated through the AutoModelForCausalLM functionality. <a href='https://huggingface.co/TabbyML/Codegen-2B' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

> **Memory requirements**: 3.129 GB (3204 MiB).

To run the `tabby-codegen-2b` service, you'll need at least a RTX 3080 GPU with 10GB of memory.

## 📒 Example Usage

<img width="367" alt="Screenshot 2023-08-01 at 11 44 31" src="https://github.com/premAI-io/prem-registry/assets/29598954/c4efe223-d21f-4d5a-a760-ea30cdf25a23">

## 🛠️ Technical Details

### 🐯 Getting Started with Tabby VSCode Extension

1. Install Tabby VSCode Extension <a href='https://huggingface.co/spaces/bigcode/license' target='_blank'>here</a>

<img width="1207" alt="Screenshot 2023-08-01 at 12 27 29" src="https://github.com/premAI-io/prem-registry/assets/29598954/05a85487-b2ad-4bcb-89fb-d610398b2f72">

2. Enable the extension and provide the URL where the service is running

<img width="1180" alt="Screenshot 2023-08-01 at 12 28 07" src="https://github.com/premAI-io/prem-registry/assets/29598954/258eaa26-78cd-41a8-a4f1-c4924f0696aa">

### 🔎 Quality Benchmarks

We evaluate our models on two code generation benchmark: HumanEval and MTPB. Please refer to the <a href='https://arxiv.org/abs/2203.13474' target='_blank'>paper</a> for more details.

### 🚫 Limitations and Biases

As an autoregressive language model, CodeGen is capable of extracting features from given natural language and programming language texts, and calculating the likelihood of them. However, the model is intended for and best at program synthesis, that is, generating executable code given English prompts, where the prompts should be in the form of a comment string. The model can complete partially-generated code as well.

## 📜 License

The model is under the 3-Clause BSD license.
