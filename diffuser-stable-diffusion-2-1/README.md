# Documentation

## 📌 Description

Stable Diffusion v2-1 is an advanced version of the Stable Diffusion v2 model, developed by Robin Rombach and Patrick Esser. This model is designed to generate and modify images based on text prompts, utilizing a Latent Diffusion Model with a fixed, pretrained text encoder (OpenCLIP-ViT/H). The model was initially fine-tuned from the Stable Diffusion v2 model and then further trained for an additional 55k steps on the same dataset (with punsafe=0.1), and then fine-tuned for another 155k extra steps with punsafe=0.98. <a href='https://stability.ai/blog/stablediffusion2-1-release7-dec-2022' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `stable-diffusion-2-1` service on Prem, you'll need access to a GPU with at least 16GiB of RAM.

## 📒 Example Usage

### 1️⃣ Prompt: Iron man portrait, highly detailed, science fiction landscape, art style by klimt and nixeu and ian sprigger and wlop and krenz cushart

![Xc3tlK4h](https://github.com/premAI-io/prem-registry/assets/29598954/3310b52f-aaeb-44fc-9bfa-9244ef6c0c6e)

### 2️⃣ Prompt: Low polygon panda 3d
![E5MREIGA](https://github.com/premAI-io/prem-registry/assets/29598954/a11d02eb-90cc-4b3c-a7a4-8c8abc988bc6)

### 3️⃣ Prompt: 3d hiper-realistic rick sanchez and morty
![zmicPjRq](https://github.com/premAI-io/prem-registry/assets/29598954/8ea64522-b255-452c-a06c-5050dfb65be6)

### 4️⃣ Prompt: Synthwave brad pitt wearing headphones, animated, trending on artstation, portrait

![pXBajmuD](https://github.com/premAI-io/prem-registry/assets/29598954/4ddb1602-bf99-4921-aeb2-f1149556e476)

## 🛠️ Technical Details

### 🚀 Getting Started with OpenAI Python client

The service exposes the same `/image/generations` (for Text-to-Image) and `image/edits` (for Prompt+Image-to-Image) endpoints as OpenAI DALL-E does. You can directly use the official `openai` python library.

#### Text-to-Image

```python

!pip install openai
!pip install pillow

import io
import base64
import openai

from PIL import Image

openai.api_base = "http://localhost:9111/v1"
openai.api_key = "random-string"

response = openai.Image.create(
    prompt="Iron man portrait, highly detailed, science fiction landscape, art style by klimt and nixeu and ian sprigger and wlop and krenz cushart",
    n=1,
    size="512x512"
)

image_string = response["data"][0]["b64_json"]

img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_string, "utf-8"))))
img.save("iron_man.jpeg")

```

#### Prompt + Image-to-Image

```python
import io
import base64
import openai

from PIL import Image

openai.api_base = "http://localhost:8000/v1"
openai.api_key = "random-string"

response = openai.Image.create_edit(
  image=open("astronaut.png", "rb"), #assuming you have an astronaut floating image
  prompt="astronaut floating in dark space, going down towards earth. Super high resolution, unreal engine, ultra realistic",
  n=1,
  guidance_scale=9,
  num_inference_steps=50,
  size="512x512",
)

image_string = response["data"][0]["b64_json"]
img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_string, "utf-8"))))
img.save("astronaut_edit.png", "PNG")
```

## 📜 License

The model is under CreativeML Open RAIL++-M License.
