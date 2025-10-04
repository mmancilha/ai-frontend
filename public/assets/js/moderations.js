document.getElementById("btnSubmit").addEventListener("click", function () {
    const moderations = document.getElementById("textUser").value;

    fetch(`http://127.0.0.1:8001/api/text/moderations?textmoderation=${moderations}`, 
    {
        method: 'POST',
        headers: { 'accept': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("responseCard").textContent = JSON.stringify(data.results[0].categories, null, 2);
    });
});
