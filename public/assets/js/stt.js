document.getElementById("btnSubmit").addEventListener("click", function () {
    const audioInput = document.getElementById("fileAudio");
    const audioFile = audioInput.files[0];

    // Transformar em Byte
    const formData = new FormData();
    formData.append("file_upload", audioFile);

    fetch('http://127.0.0.1:8001/api/audio/whisper', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("responseTranscription").textContent = data;
    });
});
