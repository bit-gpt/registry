# Documentation

## 📌 Description

Stable Diffusion x2 Latent Upscaler is a diffusion-based upscaler developed by Katherine Crowson in collaboration with Stability AI. This model was trained on a high-resolution subset of the LAION-2B dataset. It is a diffusion model that operates in the same latent space as the Stable Diffusion model, which is decoded into a full-resolution image.<a href='https://huggingface.co/stabilityai/sd-x2-latent-upscaler' target='_blank'>Learn More</a>.

## 💻 Hardware Requirements

To run the `stable-diffusion-x2-latent-upscaler` service on Prem, you'll need access to a GPU with at least 16GiB of RAM.

## 📒 Example Usage


## 🛠️ Technical Details

### 🚀 Getting Started with making requests locally

The service exposes the `/images/upscale` endpoint which can be used to upscale images. The following example shows how to:

```python
import requests
import io
import base64
from PIL import Image

url = 'http://localhost:8000/v1/images/upscale'
files = {'image': open('iron_man_image.png', 'rb')}  #assuming we have an avg resolution quality iron man image here
data = {
    'prompt': "Super high resolution image of iron man, highly detailed, real life.",
    'n': 1,
    'guidance_scale': 8
}

response = requests.post(url, files=files, data=data)
image_string = response.json()["data"][0]["b64_json"]

img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_string, "utf-8"))))
img.save("iron_man_highres.png", "PNG")

```

Or curl equivalent:
```bash
curl -X POST http://localhost:8000/v1/images/upscale \
    -F "image=@iron_man_image.png" \
    -F "prompt=Super high resolution image of iron man, highly detailed, real life." \
    -F "n=1" \
    -F "guidance_scale=8" \
    -o iron_man_highres.png
```

## 📜 License

The model is under CreativeML OpenRAIL M license is an Open RAIL M license, adapted from the work that BigScience and the RAIL Initiative are jointly carrying in the area of responsible AI licensing. See also the article about the BLOOM Open RAIL license on which our license is based.
