# Documentation

## 📌 Description

Stable Diffusion v1.5 is a sophisticated text-to-image diffusion model capable of generating high-quality images from textual prompts. Developed by Robin Rombach and Patrick Esser, this model is a significant upgrade from its predecessor, Stable Diffusion v1.2, having been fine-tuned on 595k steps at a resolution of 512x512 on `laion-aesthetics v2 5+` with a 10% drop in text-conditioning to enhance classifier-free guidance sampling. <a href='https://github.com/runwayml/stable-diffusion' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `stable-diffusion-1-5` service on Prem, you'll need access to a GPU with at least 16GiB of RAM.

## 📒 Example Usage

### 1️⃣ Prompt: Iron man portrait, highly detailed, science fiction landscape, art style by klimt and nixeu and ian sprigger and wlop and krenz cushart

![WS_USl7I](https://github.com/premAI-io/prem-registry/assets/29598954/7c31ed10-620b-445c-a23d-c34e0fa92b43)

### 2️⃣ Prompt: Low polygon panda 3d

![9rHScaSw](https://github.com/premAI-io/prem-registry/assets/29598954/bafa9c5e-02dd-4a76-8c69-d739e508ad2d)

### 3️⃣ Prompt: 3d hiper-realistic rick sanchez and morty

![PKVb4jfl](https://github.com/premAI-io/prem-registry/assets/29598954/04223540-b736-4952-9aa4-87e08759cd7d)

### 4️⃣ Prompt: Synthwave brad pitt wearing headphones, animated, trending on artstation, portrait

![35pvt7Y9](https://github.com/premAI-io/prem-registry/assets/29598954/cd49a0c4-ec50-44a4-836a-7ea4964b361e)


### Prompt: Iron man showing a wide smile + (below image)

#### Output Image:



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

The model is under CreativeML OpenRAIL M license is an Open RAIL M license, adapted from the work that BigScience and the RAIL Initiative are jointly carrying in the area of responsible AI licensing. See also the article about the BLOOM Open RAIL license on which our license is based.
