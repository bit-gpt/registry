# Documentation

## 📌 Description

Whisper Tiny is a compact version of OpenAI's Whisper model, designed for automatic speech recognition (ASR) and speech translation. Despite its smaller size, it retains the powerful capabilities of the larger models, making it suitable for applications where computational resources or storage space are limited. <a href='https://huggingface.co/openai/whisper-large-v2' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `whisper-large-v2` service on Prem, you'll just need a GPU with at least 6GiB of RAM.

## 📒 Example Usage

Whisper Tiny can be used for various tasks, including English to English transcription, French to French transcription, and French to English translation. It can also handle long-form transcription by using a chunking algorithm, allowing it to transcribe audio samples of arbitrary length.

### 🎶 sample.wav. You can find the file [here](https://github.com/premAI-io/prem-registry/blob/main/audio-to-text-whisper-tiny/sample.wav)

## 🛠️ Technical Details

### 🚀 Getting Started with OpenAI Python client

The service exposes the same endpoints as OpenAI DALL-E does. You can directly use the official `openai` python library.

```python

!pip install openai

import openai

openai.api_base = "http://184.105.5.51:10111/v1"
openai.api_key = "random-string"

audio_file = open("./sample.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)

```

## 📜 License

Whisper's code and model weights are released under the MIT License.
