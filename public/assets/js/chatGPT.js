document.getElementById("btnSubmit").addEventListener("click", function () {
    const question = document.getElementById("textUser").value;

    fetch(`http://127.0.0.1:8001/api/text/chat?message=${question}`, 
    {
        method: 'POST',
        headers: { 'accept': 'application/json' },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Erro na API");
        }
        return response.json();
    })
    .then(data => {
        // Atualiza o campo de texto com a resposta da API
        document.getElementById("textUser").value = data || "Resposta não encontrada!";
    })
    .catch(error => {
        console.error("Erro:", error);
        document.getElementById("textUser").value = "Ocorreu um erro ao processar sua solicitação.";
    });
});
