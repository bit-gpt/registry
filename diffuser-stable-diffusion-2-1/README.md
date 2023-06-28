# Documentation

## 📌 Description

Stable Diffusion v2-1 is an advanced version of the Stable Diffusion v2 model, developed by Robin Rombach and Patrick Esser. This model is designed to generate and modify images based on text prompts, utilizing a Latent Diffusion Model with a fixed, pretrained text encoder (OpenCLIP-ViT/H). The model was initially fine-tuned from the Stable Diffusion v2 model and then further trained for an additional 55k steps on the same dataset (with punsafe=0.1), and then fine-tuned for another 155k extra steps with punsafe=0.98.. <a href='https://stability.ai/blog/stablediffusion2-1-release7-dec-2022' target='_blank'>Learn More</a>.

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
