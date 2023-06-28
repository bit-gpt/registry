# Documentation

## 📌 Description

Stable Diffusion v1.5 is a sophisticated text-to-image diffusion model capable of generating high-quality images from textual prompts. Developed by Robin Rombach and Patrick Esser, this model is a significant upgrade from its predecessor, Stable Diffusion v1.2, having been fine-tuned on 595k steps at a resolution of 512x512 on `laion-aesthetics v2 5+` with a 10% drop in text-conditioning to enhance classifier-free guidance sampling. <a href='https://github.com/runwayml/stable-diffusion' target='_blank'>Learn More</a>.

## 📒 Example Usage

### 1️⃣ Prompt: Iron man portrait, highly detailed, science fiction landscape, art style by klimt and nixeu and ian sprigger and wlop and krenz cushart

### 2️⃣ Prompt: Low polygon panda 3d

### 3️⃣ Prompt: 3d hiper-realistic rick sanchez and morty

### 4️⃣ Prompt: Synthwave brad pitt wearing headphones, animated, trending on artstation, portrait

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

The model is under CreativeML OpenRAIL M license is an Open RAIL M license, adapted from the work that BigScience and the RAIL Initiative are jointly carrying in the area of responsible AI licensing. See also the article about the BLOOM Open RAIL license on which our license is based.