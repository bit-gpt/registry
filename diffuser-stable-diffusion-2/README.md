# Documentation

## 📌 Description

Stable Diffusion v2 is an enhanced version of the Stable Diffusion v2-base model, developed by Robin Rombach and Patrick Esser. This model is designed to generate and modify images based on text prompts, utilizing a Latent Diffusion Model with a fixed, pretrained text encoder (OpenCLIP-ViT/H). The model was initially trained from the Stable Diffusion v2-base model and then further trained for an additional 150k steps using a v-objective on the same dataset. It was then resumed for another 140k steps on 768x768 images. <a href='https://stability.ai/blog/stable-diffusion-v2-release' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `stable-diffusion-2` service on Prem, you'll need access to a GPU with at least 16GiB of RAM.

## 📒 Example Usage

### 1️⃣ Prompt: Iron man portrait, highly detailed, science fiction landscape, art style by klimt and nixeu and ian sprigger and wlop and krenz cushart

![k5h9_ilY](https://github.com/premAI-io/prem-registry/assets/29598954/49d162c9-a308-466c-a038-9bb54d2009fd)

### 2️⃣ Prompt: Low polygon panda 3d

![hPCoZERY](https://github.com/premAI-io/prem-registry/assets/29598954/51537f29-f4cc-469f-88c4-ad18559cb043)

### 3️⃣ Prompt: 3d hiper-realistic rick sanchez and morty

![NWVcWCfw](https://github.com/premAI-io/prem-registry/assets/29598954/667d08ad-7dd7-436f-8e2e-5e05d547653d)

### 4️⃣ Prompt: Synthwave brad pitt wearing headphones, animated, trending on artstation, portrait

![q6yKHgDv](https://github.com/premAI-io/prem-registry/assets/29598954/9b88388d-08b7-4a9a-b9a3-766497b3403a)

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

openai.api_base = "http://localhost:9222/v1"
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

openai.api_base = "http://localhost:9222/v1"
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
