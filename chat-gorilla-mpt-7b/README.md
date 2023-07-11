# 📑 Documentation

## 📌 Description
Gorilla MPT 7B is an open-source API caller trained by fine-tuning MPT weights. Given a natural language query, Gorilla can write a semantically- and syntactically- correct API to invoke. 



## 💻 Hardware Requirements

\> **Memory requirements**: 10.4 GB (10609 MiB).


To run the `gorilla-mpt-7b` service, you'll need the following hardware configuration:

### Cloud Platforms

If you are using AWS:

- Instance Type: `p3.2xlarge` or higher
- GPU: NVIDIA V100 or higher.

If you are using Paperspace:

- Instance Type: `V100-32G` or higher
- GPU: NVIDIA V100 or higher.

### On-Premise Platforms

## 📒 Example Usage

### 1️⃣ Prompt: Translate a text from English to French

\<\<\<domain\>\>\>: Natural Language Processing Text2Text Generation

\<\<\<api_call\>\>\>: T5ForConditionalGeneration.from_pretrained('google/t5-small')
 
\<\<\<api_provider\>\>\>: Hugging Face Transformers
\<\<\<explanation\>\>\>: 
1. Import the necessary classes from the transformers package, which includes T5ForConditionalGeneration for the text generation model.
2. Use the from_pretrained method to load the pre-trained model 'google/t5-small'. This model has been trained on various NLP tasks, including translation.
3. Provide an input text in English that needs to be translated to French. The model will generate a translation as output.
4. Print the translated text.
   
\<\<\<code\>\>\>:

```python
from transformers import T5ForConditionalGeneration
t5 = T5ForConditionalGeneration.from_pretrained('google/t5-small')
input_text = "Translate this text to French: I would like to learn French."
outputs = t5.generate(input_text)
translated_text = outputs[0]['generated_text']
print(translated_text)
```

### 2️⃣ Prompt: Generate an image from a prompt

Please provide a prompt for the image you would like to generate. For example: "a colorful landscape at sunset" or any other description of the desired image. The model will then generate an image based on the provided prompt, which can be saved to a file if desired.

\<\<\<domain\>\>\>: Computer Vision Image-to-Image

\<\<\<api_call\>\>\>: ControlNetModel.from_pretrained('lllyasviel/control_v11p_sd15_seg')

\<\<\<api_provider\>\>\>: Hugging Face

\<\<\<explanation\>\>\>: 
1. Import the necessary libraries and classes, such as ControlNetModel, StableDiffusionControlNetPipeline, UniPCMultistepScheduler, HfApiFlowLoader, and the Image class from the PIL package.
2. Load the ControlNet model checkpoint with the provided model name 'lllyasviel/control_v11p_sd15_seg' using the from_pretrained method.
3. Initialize the image generation pipeline by providing the loaded ControlNet model as an argument.
4. Create a prompt describing the type of image you would like to generate, such as 'a colorful landscape at sunset'.
5. Generate the image using the pipeline and the provided prompt by calling the pipeline with the prompt and number of inference steps.
6. Save the generated image to a file if desired.

\<\<\<code\>\>\>: 

```python
from diffusers import ControlNetModel, StableDiffusionControlNetPipeline, UniPCMultistepScheduler
from diffusers.utils import load_image
from huggingface_hub import HfApiFlowLoader
from PIL import Image
checkpoint = 'lllyasviel/control_v11p_sd15_seg'
controlnet = ControlNetModel.from_pretrained(checkpoint)
pipe = StableDiffusionControlNetPipeline.from_pretrained('runwayml/stable-diffusion-v1-5', controlnet=controlnet)
pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
generator = torch.manual_seed(0)
prompt = 'a colorful landscape at sunset'
image = pipe(prompt, num_inference_steps=30, generator=generator).images[0]
image.save('landscape_sunset.png')
```

### 3️⃣ Prompt: Upscale an image

1. To upscale an image, you can use the 'ImageProcessor.from_pretrained' method from the transformers package. 
2. Import the required libraries, which include 'Image' from PIL, 'ImageProcessor' from transformers, and 'torch' for processing tensors. 
3. Load the input image using the 'Image.open' method from PIL. You can open a file or get the image data from a URL. 
4. Create an 'ImageProcessor' instance using the 'ImageProcessor.from_pretrained' method with the model name 'google/upsample_sd15_b2_canny'. This model is designed for Canny edge detection and will upscale images by a factor of 2. 
5. Process the input image with the 'processor' instance and save the upscaled image to a file. 
   
\<\<\<domain\>\>\>: Computer Vision Image-to-Image

\<\<\<api_call\>\>\>: 

```python
from transformers import ImageProcessor, CLIPModel
from PIL import Image
import torch
processor = ImageProcessor.from_pretrained('google/upsample_sd15_b2_canny')
model = CLIPModel.from_pretrained('openai/clip-vit-large-patch14')
input_image = Image.open('input_image_path.jpg')
# replace 'input_image_path.jpg' with the path to your image
processor(input_image, return_tensors='pt')
upscaled_image = model.generate(processor.images, num_inference_steps=20)
upscaled_image.save('output_image_path.jpg')
```

### 4️⃣ Prompt: Our customer is a zoo and we want to help them detect movement of different animals. Write a python program in 1 to 2 lines to call API in TensorFlowHub.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
model = AutoModelForSequenceClassification.from_pretrained('setu4993/xlm-roberta-base-animal-detection')
tokenizer = AutoTokenizer.from_pretrained('setu4993/xlm-roberta-base-animal-detection')
processor = pipeline('setu4993/xlm-roberta-base-animal-detection', model=model, tokenizer=tokenizer)
inputs = processor(input_text, return_tensors='pt')
outputs = model(**inputs)
```

## 🛠️ Technical Details

### 🦜🔗 Getting Started with Langchain

```bash
pip install langchain openai
```

It can be run simply using the langchain library as shown below:

```python
import os
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "random-string"

chat = ChatOpenAI(openai_api_base="http://localhost:8000/v1")
messages = [HumanMessage(content="Generate an image from a text")]
print(chat(messages))

# output:
# <<<domain>>>: Multimodal Text-to-Image Generation
# <<<api_call>>>: StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4', vae='AutoencoderKL.from_pretrained(stabilityai/sd-vae-ft-mse)')
# <<<api_provider>>>: Hugging Face
# <<<explanation>>>:1. Import the necessary libraries: AutoencoderKL from diffusers.models and StableDiffusionPipeline from diffusers.
# 2. Load the 'CompVis/stable-diffusion-v1-4' model and the'stabilityai/sd-vae-ft-mse' VAE model. The VAE model will be used for text encoding.
# 3. Create a StableDiffusionPipeline instance by calling the from_pretrained method with the model and VAE as arguments.
# 4. Provide a text prompt describing the desired image, and use the pipeline to generate an image based on the text prompt. Save the generated image to a file.
```

For using it in a chat setting we recommend using a Chat Prompt Template as shown below:
    
```python

import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "random-string"

chat_template = """
User: {user_message}
Assistant: 
"""
prompt = PromptTemplate(
    input_variables=["user_message"],
    template=chat_template,
)

user_message = "Generate an image from a text"

chat = ChatOpenAI(openai_api_base="http://localhost:8000/v1")
chain = LLMChain(llm=chat, prompt=prompt, verbose=True)
print(chain.run(user_message=user_message))

# output: \> Finished chain.
# <<<domain>>>: Multimodal Text-to-Image Generation
# <<<api_call>>>: StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4', vae='AutoencoderKL.from_pretrained(stabilityai/sd-vae-ft-mse)')
# <<<api_provider>>>: Hugging Face
# <<<explanation>>>:1. Import the necessary libraries: AutoencoderKL from diffusers.models and StableDiffusionPipeline from diffusers.
# 2. Load the 'CompVis/stable-diffusion-v1-4' model and the'stabilityai/sd-vae-ft-mse' VAE model. The VAE model will be used for text encoding.
# 3. Create a StableDiffusionPipeline instance by calling the from_pretrained method with the model and VAE as arguments.
# 4. Provide a text prompt describing the desired image, and use the pipeline to generate an image based on the text prompt. Save the generated image to a file.

```

### 🚫 Limitations and Biases

We have noticed that the model sometimes generates responses with reference to some random unexisting model name on Huggingface(e.g. in the last prompt the model `setu4993/xlm-roberta-base-animal-detection` does not exists).  Furthermore also the structure  of the output is not always the same (refer to above prompt examples).
We recommend users of Gorilla models to develop guardrails and to take appropriate precautions for any production use.

The creators of Gorilla Falcon 7B have mentioned that despite their effort in addressing the risks of hallucinations like other LLMs, Gorilla models are not free from such limitations. We hope our open-sourced codebase will help other researchers better understand these challenges and improve on these key limitations for making AI beneficial for everyone.


## 📜 License
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.