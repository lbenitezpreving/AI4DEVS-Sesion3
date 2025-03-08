# Backend del Sistema de Gestión de Candidatos (ATS) - LTI

Este directorio contiene el código del backend para el Sistema de Seguimiento de Candidatos (ATS) de LTI, desarrollado con FastAPI y PostgreSQL.

## Estructura del proyecto

El proyecto sigue una arquitectura de Domain-Driven Design (DDD):

```
backend/
├── migrations/           # Migraciones de Alembic
├── src/                  # Código fuente
│   ├── domain/           # Modelos de dominio y esquemas
│   ├── application/      # Servicios y repositorios
│   ├── infrastructure/   # Configuración de infraestructura
│   └── interfaces/       # Interfaces de usuario (API)
├── tests/                # Pruebas unitarias e integración
├── .env                  # Variables de entorno
├── alembic.ini           # Configuración de Alembic
├── requirements.txt      # Dependencias del proyecto
└── run.py                # Script para ejecutar la aplicación
```

## Requisitos previos

- Python 3.10 o superior
- PostgreSQL 15 o superior
- Docker (opcional, para ejecutar PostgreSQL)

## Instalación

1. Crear un entorno virtual:

```bash
python -m venv venv
```

2. Activar el entorno virtual:

```bash
# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar las variables de entorno (o usar el archivo .env proporcionado)

## Base de datos

1. Iniciar la base de datos PostgreSQL con Docker:

```bash
cd ../database
docker-compose up -d
```

2. Ejecutar las migraciones:

```bash
cd ../backend
alembic upgrade head
```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
python run.py
```

La API estará disponible en http://localhost:8000

## Documentación de la API

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

Para ejecutar las pruebas con cobertura:

```bash
pytest --cov=src
``` 