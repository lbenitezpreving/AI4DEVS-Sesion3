import os
import uvicorn
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la aplicación
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

if __name__ == "__main__":
    print(f"Iniciando servidor en {API_HOST}:{API_PORT} (DEBUG: {DEBUG})")
    uvicorn.run("src.main:app", host=API_HOST, port=API_PORT, reload=DEBUG) 