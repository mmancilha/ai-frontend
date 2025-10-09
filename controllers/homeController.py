from fastapi import APIRouter, Request  # Importa a classe APIRouter e Request do FastAPI
from fastapi.responses import HTMLResponse  # Importa a classe HTMLResponse do FastAPI para respostas HTML
from fastapi.templating import Jinja2Templates  # Importa a classe Jinja2Templates do FastAPI para renderização de templates

# Cria um roteador para as rotas da página inicial
router = APIRouter()

# Define o diretório de templates para o Jinja2
templates = Jinja2Templates(directory="public")
# templates = Jinja2Templates(directory="public/template")


# Rota para a página inicial
@router.get("/jinja2", response_class=HTMLResponse)
async def index(request: Request):
    # Renderiza o template 'index.html' e passa o objeto 'request'
    return templates.TemplateResponse("view/teste.html", {"request": request})


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/home.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/chat", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/chat.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/imagegeneration", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/imagegeneration.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/moderations", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/moderation.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/stt", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/stt.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/tts", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/tts.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/sobre", response_class=HTMLResponse)
async def index(request: Request):
    # Abre o arquivo HTML e retorna o conteúdo como resposta HTML
    with open("public/view/sobre.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

