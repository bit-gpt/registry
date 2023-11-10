# Documentation

## 📌 Description

Whisper is a pre-trained model for automatic speech recognition (ASR) and speech translation. Trained on 680k hours of labelled data, Whisper Large demonstrate a strong ability to generalise to many datasets and domains without the need for fine-tuning. <a href='https://huggingface.co/openai/whisper-large-v2' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `whisper-large-cpp` service on Prem, you'll just need a CPU with around 4.7GiB of RAM.

## 📒 Example Usage

Whisper Large V2 can be used for various tasks, including English to English transcription, French to French transcription, and French to English translation. It can also handle long-form transcription by using a chunking algorithm, allowing it to transcribe audio samples of arbitrary length.

### 🎶 sample.wav. You can find the file [here](https://github.com/premAI-io/prem-registry/blob/main/audio-to-text-whisper-tiny/sample.wav)

<img width="1449" alt="image" src="https://github.com/premAI-io/prem-registry/assets/29598954/4b879d6b-4404-47ae-b3c9-f2f5fd38ec0e">

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
