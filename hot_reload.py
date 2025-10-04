import os
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import signal
import sys
import threading

class HotReloadHandler(FileSystemEventHandler):
    def __init__(self, server_process=None):
        self.server_process = server_process
        self.last_reload = 0
        self.reload_delay = 1  # Delay de 1 segundo para evitar múltiplos reloads
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        # Filtrar apenas arquivos relevantes
        file_path = Path(event.src_path)
        if file_path.suffix in ['.html', '.css', '.js', '.py']:
            current_time = time.time()
            if current_time - self.last_reload > self.reload_delay:
                self.last_reload = current_time
                print(f"📁 Arquivo modificado: {file_path.name}")
                print("🔄 Recarregando servidor...")
                self.restart_server()
    
    def restart_server(self):
        if self.server_process:
            try:
                # Terminar o processo atual
                self.server_process.terminate()
                self.server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.server_process.kill()
            except Exception as e:
                print(f"Erro ao terminar servidor: {e}")
        
        # Iniciar novo processo
        try:
            self.server_process = subprocess.Popen([
                "uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"
            ], cwd=os.getcwd())
            print("✅ Servidor reiniciado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao reiniciar servidor: {e}")

def start_hot_reload():
    print("🚀 Iniciando Hot Reload para FrontAI...")
    print("📂 Monitorando pasta 'public' para mudanças em HTML, CSS e JS")
    print("🔧 Monitorando arquivos Python para mudanças no backend")
    print("⏹️  Pressione Ctrl+C para parar\n")
    
    # Iniciar servidor uvicorn
    server_process = subprocess.Popen([
        "uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"
    ], cwd=os.getcwd())
    
    # Configurar handler
    event_handler = HotReloadHandler(server_process)
    observer = Observer()
    
    # Monitorar pasta public
    public_path = Path("public")
    if public_path.exists():
        observer.schedule(event_handler, str(public_path), recursive=True)
        print(f"👀 Monitorando: {public_path.absolute()}")
    
    # Monitorar arquivos Python (controllers, etc.)
    controllers_path = Path("controllers")
    if controllers_path.exists():
        observer.schedule(event_handler, str(controllers_path), recursive=True)
        print(f"👀 Monitorando: {controllers_path.absolute()}")
    
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Parando Hot Reload...")
        observer.stop()
        if server_process:
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()
        print("✅ Hot Reload parado com sucesso!")
    
    observer.join()

if __name__ == "__main__":
    start_hot_reload()