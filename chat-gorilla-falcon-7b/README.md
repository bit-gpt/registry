# 📑 Documentation

## 📌 Description
Gorilla Falcon 7B is an open-source API caller trained by fine-tuning Falcon weights. Given a natural language query, Gorilla can write a semantically- and syntactically- correct API to invoke. 



## 💻 Hardware Requirements

**Memory requirements**: 10.6 GB (10874 MiB).


To run the `gorilla-falcon-7b` service, you'll need the following hardware configuration:

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

\<\<\<api_call\>\>\>: T5ForConditionalGeneration.from_pretrained('google/byt5-small')

\<\<\<api_provider\>\>\>: Hugging Face Transformers

1. Import the necessary classes from the transformers package, which includes T5Tokenizer and T5ForConditionalGeneration.
2. Load the pre-trained model 'google/byt5-small' using T5ForConditionalGeneration.from_pretrained() method. This model is specifically designed for text-to-text generation tasks.
3. Load the tokenizer associated with the model using T5Tokenizer.from_pretrained('google/byt5-small') method.
4. Prepare the input text by adding the prefix 'translate English to French:'before the text you want to translate.
5. Tokenize the input text using the tokenizer and generate the output text using the model.
6. Decode the output tokens to obtain the translated French text.

### 2️⃣ Prompt: Generate an image from a prompt

\<\<\<domain\>\>\>: Multimodal Text-to-Image

\<\<\<api_call\>\>\>: StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4')

\<\<\<api_provider\>\>\>: Hugging Face
1. Import the StableDiffusionPipeline class from the diffusers package and Image class from PIL.
2. Load the pretrained StableDiffusionPipeline model with the identifier 'CompVis/stable-diffusion-v1-4'.
3. Provide the text prompt describing the image you want to generate. For example, 'a beautiful landscape with a mountain range and a river'.
4. Use the pipeline to generate an image based on the provided prompt. The generated image will be stored in the variable 'image'. You can then save the image to a file if needed.

### 3️⃣ Prompt: Upscale an image

\<\<\<domain\>\>\>: Computer Vision Image-to-Image

\<\<\<api_call\>\>\>: pipeline('image-super-resolution', model='caidas/swin2SR-classical-sr-x4-64')

\<\<\<api_provider\>\>\>: Hugging Face Transformers
1. Import the necessary libraries, which include the 'pipeline' function from transformers and the 'Image' class from PIL.
2. Use the 'pipeline' function to create an instance of the 'image-super-resolution' model with the pre-trained 'caidas/ swin2SR-classical-sr-x4-64' model. This model is designed to upscale images by a factor of 4.
3. Load the input image into the 'Image' class and pass it to the model for upscaling.
4. The upscaled image will be saved in the same file with the prefix 'upscaled_'.


### 4️⃣ Prompt: Our customer is a zoo and we want to help them detect movement of different animals. Write a python program in 1 to 2 lines to call API in TensorFlowHub.

```python
# Import required libraries 'AutoImageProcessor' and 'PredictionLayer' from transformers, 'Image' from PIL, and'requests'. Load the animal detection image from a URL.
processor = AutoImageProcessor.from_pretrained('hf-tiny-model-private/tiny-random-CLIPSegModel')
model = PredictionLayer.from_pretrained('hf-tiny-model-private/tiny-random-CLIPSegModel')
image_url = 'https://example.com/animal_image.jpg'  # Replace this with the URL of the image you want to analyze.
image = Image.open(requests.get(image_url, stream=True).raw)  # Read the image from the URL and convert it to PIL Image format.
inputs = processor(images=image, return_tensors='pt')  # Prepare inputs for the model by processing the image and converting it to the required format.
outputs = model(**inputs)  # Apply the model to the inputs and obtain the output.
# Analyze output for animal detections and take appropriate action.
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
# \<\<\<domain\>\>\>: Multimodal Text-to-Image Generation
# \<\<\<api_call\>\>\>: StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4', vae='AutoencoderKL.from_pretrained(stabilityai/sd-vae-ft-mse)')
# \<\<\<api_provider\>\>\>: Hugging Face
# \<\<\<explanation\>\>\>:1. Import the necessary libraries: AutoencoderKL from diffusers.models and StableDiffusionPipeline from diffusers.
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

# output: Finished chain.
# \<\<\<domain\>\>\>: Multimodal Text-to-Image Generation
# \<\<\<api_call\>\>\>: StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4', vae='AutoencoderKL.from_pretrained(stabilityai/sd-vae-ft-mse)')
# \<\<\<api_provider\>\>\>: Hugging Face
# \<\<\<explanation\>\>\>:1. Import the necessary libraries: AutoencoderKL from diffusers.models and StableDiffusionPipeline from diffusers.
# 2. Load the 'CompVis/stable-diffusion-v1-4' model and the'stabilityai/sd-vae-ft-mse' VAE model. The VAE model will be used for text encoding.
# 3. Create a StableDiffusionPipeline instance by calling the from_pretrained method with the model and VAE as arguments.
# 4. Provide a text prompt describing the desired image, and use the pipeline to generate an image based on the text prompt. Save the generated image to a file.

```

### 🚫 Limitations and Biases

We have noticed that the model sometimes generates responses with reference to some random unexisting model name on Huggingface. Furthermore also the structure  of the output is not always the same (refer to above prompt examples). 
We recommend users of Gorilla models to develop guardrails and to take appropriate precautions for any production use.

The creators of Gorilla Falcon 7B have mentioned that despite their effort in addressing the risks of hallucinations like other LLMs, Gorilla models are not free from such limitations. We hope our open-sourced codebase will help other researchers better understand these challenges and improve on these key limitations for making AI beneficial for everyone.


## 📜 License
It is made available under a permissive Apache 2.0 license allowing for commercial use, without any royalties or restrictions.