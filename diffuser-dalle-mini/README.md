# Documentation

## 📌 Description

Dall-E Mini is a text-to-image model attempt at reproducing OpenAI's DALL-E model results with an Open Source model. The model is trained by looking at millions of images from the internet with their associated captions. Over time, it learns how to draw an image from a text prompt.
Some concepts are learned from memory as they may have seen similar images. However, it can also learn how to create unique images that don't exist, such as "the Eiffel tower is landing on the moon," by combining multiple concepts together. A project report on the same by the creators can be found <a href='https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-mini-Generate-images-from-any-text-prompt--VmlldzoyMDE4NDAy' target='_blank'>here</a>

## 💻 Hardware Requirements

To run the `dalle-mini` service on Prem, you'll need access to a GPU with at least 32GiB of RAM.

## 📒 Example Usage

### 1️⃣ Prompt: hot tonkotsu ramen bowl, top view
![hot_tonkotsu_ramen_bowl_top_view](https://github.com/premAI-io/prem-registry/assets/35634788/d89b8a7b-354b-474d-8df1-67475f9311cf)

### 2️⃣ Prompt: an illustration of doggo wearing a spacesuit
![an_illustration_of_doggo_wearing_a_spacesuit](https://github.com/premAI-io/prem-registry/assets/35634788/bbb44e88-ceef-4fce-8017-f727bbfdc874)

## 🛠️ Technical Details

### 🚀 Getting Started with OpenAI Python client

The service exposes the same endpoints as OpenAI DALL-E does. You can directly use the official `openai` python library.

```python

!pip install openai
!pip install pillow

import io
import base64
import openai

from PIL import Image

openai.api_base = "http://localhost:8600/v1"
openai.api_key = "random-string"

response = response = openai.Image.create(
    prompt="an illustration of doggo wearing a spacesuit",
    n=1
)

image_string = response["data"][0]["b64_json"]

img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_string, "utf-8"))))
img.save("space_doggo.png", format="PNG")

```

## 📜 License
It's released under Apache 2.0 License, which enables commercial usage.
