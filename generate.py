import codecs
import json
import os

from markdown import markdown

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

with open("manifests.json", "w") as f:
    json.dump(manifests, f)
