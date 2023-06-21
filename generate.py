import codecs
import json
import os
import sys

APPS = ["chat", "vector-store", "coder", "embeddings",
        "diffuser", "text-to-audio", "audio-to-text"]

manifests = []
for folder in os.listdir("."):
    folder_path = os.path.join(".", folder)
    if os.path.isdir(folder_path) and any(s in folder_path for s in APPS):
        manifest_path = os.path.join(folder_path, "manifest.json")
        readme_path = os.path.join(folder_path, "README.md")
        logo_path = os.path.join(folder_path, "logo.svg")

        with open(manifest_path) as f:
            manifest = json.load(f)

        with codecs.open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
            manifest["documentation"] = readme_content

        if os.path.exists(logo_path):
            manifest[
                "icon"
            ] = f"https://raw.githubusercontent.com/premAI-io/prem-registry/{sys.argv[1]}/{folder}/logo.svg"
        else:
            manifest["icon"] = None

        manifests.append(manifest)

with open("manifests.json", "w") as f:
    json.dump(manifests, f)
