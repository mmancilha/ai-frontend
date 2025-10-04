document.getElementById("btnSubmit").addEventListener("click", function () {
    const textarea = document.getElementById("textUser").value;

    fetch(`http://127.0.0.1:8001/api/vision/imggeneration?prompt_image=${textarea}`, 
    {
        method: 'POST',
        headers: { 'accept': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("textUser").value = data;
    });
});
