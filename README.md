# Prem Registry

The repository contains all the services that are exposed and used through the Prem Controller. To learn more about Prem visit https://github.com/premAI-io/prem-box.

## Packaging a Service for Prem Registry

1. Clone the repo locally

```bash
git clone https://github.com/premAI-io/prem-registry
cd prem-registry
```

2. Create a new branch using the app and service id e.g., `prem-chat-vicuna-7b-q4`. It should only contain lowercase alphabetical characters and dashes. You should follow the format `{app}-{id}`.

```bash
git checkout -b prem-chat-vicuna-7b-q4
```

3. Create the files necessary for submission

- `manifest.json` - It contains all the service metadata in order to run the service inside `prem-box`.
- `README.md` - Documentation for the service. It will show up in the Service Detail view.
- `logo.svg` - 256x256 Logo in SVG format.

Here an example of `manifest.json`

```json
{
    "id": "vicuna-7b-q4",
    "name": "Vicuna 7B Q4",
    "description": "Vicuna 7B Q4",
    "documentation": "",
    "icon": "",
    "modelInfo": {
            "maxLength": 12000,
        "tokenLimit": 4000,
        "weightsName": "vicuna-7b-q4.bin",
        "weightsSize": 4212859520,
        "devices": ["m1"],
        "memoryRequirements": "8gb",
        "inferenceTime": "5 tokens per second"
    },
    "apps": ["chat", "embeddings"],
    "dockerImage": "ghcr.io/premai-io/prem-chat-vicuna-7b-q4-m1:latest",
    "defaultPort": 8001
}
```

4. Create the Pull Request

Create a pull request providing basic information.

## FAQs
