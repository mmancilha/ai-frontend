document.getElementById("btnSubmit").addEventListener("click", function () {
    const valueText = document.getElementById("textUser").value;

    fetch(`http://127.0.0.1:8001/api/audio/tts?text=${valueText}`, 
    {
        method: 'POST',
        headers: { 'accept': 'application/json' },
    })
    .then(response => response.blob()) // Obtém o blob do áudio da resposta
    .then(blob => {
        // Cria uma URL para o blob (áudio)
        const audioURL = URL.createObjectURL(blob);

        // Cria o elemento de áudio no HTML
        const audioElement = document.createElement("audio");
        audioElement.src = audioURL;
        audioElement.controls = true;

        // Cria um contêiner (DIV) para o áudio
        const audioContainer = document.createElement("div");
        audioContainer.id = "audioContainer";
        audioContainer.classList.add("container", "mt-5");

        // Adiciona os elementos ao DOM
        document.body.appendChild(audioContainer);
        audioContainer.appendChild(audioElement);
    })
    .catch(error => {
        console.error("Erro:", error);
    });
});
