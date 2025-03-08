import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.interfaces.api.routes.candidates import router as candidates_router
from src.interfaces.api.routes.job_positions import router as job_positions_router
from src.interfaces.api.routes.applications import router as applications_router
from src.interfaces.api.routes.interviews import router as interviews_router

# Cargar variables de entorno
load_dotenv()

# Configuración de la aplicación
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

# Crear la aplicación FastAPI
app = FastAPI(
    title="LTI ATS API",
    description="API para el Sistema de Seguimiento de Candidatos (ATS) de LTI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    debug=DEBUG,
)

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:4200",  # Frontend Angular
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(candidates_router)
app.include_router(job_positions_router)
app.include_router(applications_router)
app.include_router(interviews_router)

# Ruta raíz
@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API del Sistema de Seguimiento de Candidatos (ATS) de LTI",
        "version": "1.0.0",
        "environment": ENVIRONMENT,
        "docs": "/docs",
    }

# Para ejecutar la aplicación directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host=API_HOST, port=API_PORT, reload=DEBUG) 