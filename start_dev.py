#!/usr/bin/env python3
"""
Script para iniciar o servidor FastAPI com Hot Reload completo
Monitora mudanças em arquivos HTML, CSS, JS e Python
"""

import os
import sys
import subprocess
import signal
from pathlib import Path

def start_dev_server():
    """Inicia o servidor de desenvolvimento com hot reload"""
    print("🚀 Iniciando FrontAI em modo de desenvolvimento...")
    print("📂 Hot Reload ativo para:")
    print("   • Arquivos Python (.py) - Backend")
    print("   • Arquivos HTML (.html) - Frontend")
    print("   • Arquivos CSS (.css) - Estilos")
    print("   • Arquivos JavaScript (.js) - Scripts")
    print("\n🌐 Servidor disponível em: http://127.0.0.1:8000")
    print("⏹️  Pressione Ctrl+C para parar\n")
    
    try:
        # Usar uvicorn com configurações otimizadas para desenvolvimento
        cmd = [
            "uvicorn", 
            "main:app", 
            "--reload",
            "--reload-dir", "public",
            "--reload-dir", "controllers",
            "--reload-dir", ".",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--log-level", "info"
        ]
        
        # Executar o comando
        process = subprocess.run(cmd, cwd=os.getcwd())
        
    except KeyboardInterrupt:
        print("\n🛑 Parando servidor de desenvolvimento...")
        print("✅ Servidor parado com sucesso!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_dev_server()