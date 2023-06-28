# Documentation

## 📌 Description

Stable Diffusion v2 is an enhanced version of the Stable Diffusion v2-base model, developed by Robin Rombach and Patrick Esser. This model is designed to generate and modify images based on text prompts, utilizing a Latent Diffusion Model with a fixed, pretrained text encoder (OpenCLIP-ViT/H). The model was initially trained from the Stable Diffusion v2-base model and then further trained for an additional 150k steps using a v-objective on the same dataset. It was then resumed for another 140k steps on 768x768 images. <a href='https://stability.ai/blog/stable-diffusion-v2-release' target='_blank'>Learn More</a>.

## 📒 Example Usage

### 1️⃣ Prompt: Iron man portrait, highly detailed, science fiction landscape, art style by klimt and nixeu and ian sprigger and wlop and krenz cushart

![WS_USl7I](https://github.com/premAI-io/prem-registry/assets/29598954/7c31ed10-620b-445c-a23d-c34e0fa92b43)

### 2️⃣ Prompt: Low polygon panda 3d

![9rHScaSw](https://github.com/premAI-io/prem-registry/assets/29598954/bafa9c5e-02dd-4a76-8c69-d739e508ad2d)

### 3️⃣ Prompt: 3d hiper-realistic rick sanchez and morty

![PKVb4jfl](https://github.com/premAI-io/prem-registry/assets/29598954/04223540-b736-4952-9aa4-87e08759cd7d)

### 4️⃣ Prompt: Synthwave brad pitt wearing headphones, animated, trending on artstation, portrait

![35pvt7Y9](https://github.com/premAI-io/prem-registry/assets/29598954/cd49a0c4-ec50-44a4-836a-7ea4964b361e)

## 🛠️ Technical Details

### 🚀 Serving Details

The service exposes the same endpoints as OpenAI DALL-E does. You can directly use the official `openai` python library.

```python

!pip install openai

import os
import openai

openai.api_key = "random-string"

openai.Image.create(
  prompt="A cute baby sea otter",
  n=1,
  size="512x512"
)
```

## 📜 License

The model is under CreativeML Open RAIL++-M License.
