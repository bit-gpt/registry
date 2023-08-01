# 📑 Documentation

## 📌 Description

CodeGen-Multi 2B is part of the CodeGen family, specifically designed for program synthesis in languages like C, C++, Go, Java, JavaScript, and Python. Initialized with CodeGen-NL 2B, it was further pre-trained on BigQuery with 119.2B tokens, utilizing cross-entropy loss and multiple TPU-v4-512 by Google. Best suited for generating executable code from English prompts, it can also complete partially-generated code. Loading and utilization are facilitated through the AutoModelForCausalLM functionality. <a href='https://huggingface.co/TabbyML/Codegen-2B' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

> **Memory requirements**: 3.129 GB (3204 MiB).

To run the `tabby-codegen-2b` service, you'll need at least a RTX 3080 GPU with 10GB of memory.

## 📒 Example Usage

IMAGE

## 🛠️ Technical Details

### 🐯 Getting Started with Tabby VSCode Extension

1. Install Tabby VSCode Extension <a href='https://marketplace.visualstudio.com/items?itemName=TabbyML.vscode-tabby' target='_blank'>here</a>

IMAGE

2. Enable the extension and provide the URL where the service is running

IMAGE

### 🔎 Quality Benchmarks

We evaluate our models on two code generation benchmark: HumanEval and MTPB. Please refer to the <a href='https://arxiv.org/abs/2203.13474' target='_blank'>paper</a> for more details.

### 🚫 Limitations and Biases

As an autoregressive language model, CodeGen is capable of extracting features from given natural language and programming language texts, and calculating the likelihood of them. However, the model is intended for and best at program synthesis, that is, generating executable code given English prompts, where the prompts should be in the form of a comment string. The model can complete partially-generated code as well.

## 📜 License

The model is under the 3-Clause BSD license.