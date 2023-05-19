fetch("https://prem-registry.fly.dev/manifests/")
    .then(response => response.json())
    .then(data => {
        const manifestsDiv = document.getElementById('manifests');

        data.forEach(manifest => {
            const card = document.createElement('div');
            card.className = 'card';

            if (manifest.icon) {
                const img = document.createElement('img');
                img.src = manifest.icon;
                img.alt = manifest.name;
                card.appendChild(img);
            }

            const h2 = document.createElement('h2');
            h2.textContent = manifest.name;
            card.appendChild(h2);

            if (manifest.description) {
                const p = document.createElement('p');
                p.textContent = manifest.description;
                card.appendChild(p);
            }

            if (manifest.documentation) {
                const a = document.createElement('a');
                a.href = manifest.documentation;
                a.textContent = "Documentation";
                a.target = "_blank";
                card.appendChild(a);
            }

            if (manifest.modelInfo) {
                for (const info in manifest.modelInfo) {
                    const p = document.createElement('p');
                    p.textContent = `${info}: ${manifest.modelInfo[info]}`;
                    card.appendChild(p);
                }
            }

            if (manifest.apps && manifest.apps.length > 0) {
                const p = document.createElement('p');
                p.textContent = `Apps: ${manifest.apps.join(", ")}`;
                card.appendChild(p);
            }

            if (manifest.dockerImage) {
                const p = document.createElement('p');
                p.textContent = `Docker Image: ${manifest.dockerImage}`;
                card.appendChild(p);
            }

            if (manifest.defaultPort) {
                const p = document.createElement('p');
                p.textContent = `Default Port: ${manifest.defaultPort}`;
                card.appendChild(p);
            }

            manifestsDiv.appendChild(card);
        });
    })
    .catch(error => console.error(`Error: ${error}`));
