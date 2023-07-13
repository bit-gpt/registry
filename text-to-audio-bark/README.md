# Documentation

## 📌 Description

Bark is a transformer-based text-to-audio model created by Suno https://suno.ai/. Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise, and simple sound effects. <a href='https://github.com/suno-ai/bark' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `bark` service on Prem, you'll just need a GPU or CPU with at least 6GiB of RAM.

## 📒 Example Usage

### 2️⃣ Prompt: Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.

[pizza1.webm](https://user-images.githubusercontent.com/34592747/cfa98e54-721c-4b9c-b962-688e09db684f.webm)

## 🛠️ Technical Details

### 🚀 Getting Started with Python

```python

import requests

prompt = """
Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
But I also have other interests such as playing tic tac toe.
"""

response = requests.post("http://localhost:10111/v1/audio/generation",
                         json={"prompt": prompt})
response_content = requests.get(
    f"http://localhost:10111/files/{response.json()['url']}")

with open("output_file.wav", "wb") as f:
    f.write(response_content.content)

```

## 📜 License

Bark was developed for research purposes. It is not a conventional text-to-speech model but instead a fully generative text-to-audio model, which can deviate in unexpected ways from provided prompts. Bark is licensed under the MIT License.
