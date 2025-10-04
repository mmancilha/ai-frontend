from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

from controllers.homeController import router as home_router


app = FastAPI()


# Montar o diretório de arquivos estáticos
app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")

# Configurar hot reload para desenvolvimento
if os.getenv("ENVIRONMENT", "development") == "development":
    # Adicionar middleware para hot reload
    from fastapi.middleware.cors import CORSMiddleware
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(home_router)




