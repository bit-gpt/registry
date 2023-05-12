import codecs
import json
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from markdown import markdown
from pydantic import BaseModel


class Manifest(BaseModel):
    id: str
    name: str
    description: str
    documentation: str
    icon: str
    modelInfo: dict
    apps: list[str]
    dockerImage: str
    defaultPort: int


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manifests = []

app.mount("/logos", StaticFiles(directory="."), name="logos")


@app.on_event("startup")
async def load_manifests():
    global manifests
    manifests = []
    for folder in os.listdir("."):
        folder_path = os.path.join(".", folder)
        if os.path.isdir(folder_path) and "prem" in folder_path:
            manifest_path = os.path.join(folder_path, "manifest.json")
            readme_path = os.path.join(folder_path, "README.md")
            logo_path = os.path.join(folder_path, "logo.svg")

            with open(manifest_path) as f:
                manifest = json.load(f)

            with codecs.open(readme_path, "r", encoding="utf-8") as f:
                readme_content = f.read()
                manifest["documentation"] = markdown(readme_content)

            if os.path.exists(logo_path):
                manifest["icon"] = f"/logos/{folder}/logo.svg"
            else:
                manifest["icon"] = None

            manifests.append(manifest)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/manifests/", response_model=list[Manifest])
async def get_manifests():
    return manifests


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
