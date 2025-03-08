# Sistema de Gestión de Candidatos (ATS) - LTI

## Descripción
Este proyecto implementa un Sistema de Seguimiento de Candidatos (ATS - Applicant Tracking System) para la empresa LTI. El sistema permite gestionar de manera eficiente el proceso de reclutamiento y selección de personal, desde la publicación de vacantes hasta la contratación de candidatos.

## Características principales
- Gestión completa del ciclo de vida de reclutamiento
- Seguimiento de candidatos en diferentes etapas del proceso
- Evaluación y calificación de candidatos
- Generación de reportes y análisis
- Interfaz de usuario intuitiva y responsive

## Arquitectura
El proyecto sigue una arquitectura de microservicios con:
- **Frontend**: Desarrollado en Angular 16
- **Backend**: Desarrollado en Python con FastAPI
- **Base de datos**: PostgreSQL 15

## Metodología
El desarrollo se realiza siguiendo:
- **Domain-Driven Design (DDD)**: Para modelar el dominio del negocio
- **Test-Driven Development (TDD)**: Para asegurar la calidad del código
- **Control de versiones con Git**: Para gestionar los cambios en el código

## Estructura del proyecto
```
├── backend/         # Servicios backend en Python/FastAPI
├── frontend/        # Aplicación frontend en Angular
├── database/        # Scripts y configuración de la base de datos
└── docs/            # Documentación del proyecto
```

## Requisitos previos
- Python 3.10 o superior
- Node.js 18 o superior
- npm 9 o superior
- Docker y Docker Compose (para la base de datos)
- Git

## Instalación y configuración

### Base de datos
1. Navegar al directorio de la base de datos:
```bash
cd database
```

2. Iniciar la base de datos con Docker Compose:
```bash
docker-compose up -d
```

La base de datos PostgreSQL estará disponible en `localhost:5432` con las siguientes credenciales:
- Usuario: `lti_admin`
- Contraseña: `lti_password_secure`
- Base de datos: `lti_ats_db`

### Backend
1. Navegar al directorio del backend:
```bash
cd backend
```

2. Crear y activar un entorno virtual:
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:
```bash
alembic upgrade head
```

5. Iniciar el servidor:
```bash
python run.py
```

El backend estará disponible en `http://localhost:8000`

### Frontend
1. Navegar al directorio del frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Iniciar el servidor de desarrollo:
```bash
ng serve
```

El frontend estará disponible en `http://localhost:4200`

## Documentación
- API Backend: `http://localhost:8000/docs` (Swagger UI)
- API Backend: `http://localhost:8000/redoc` (ReDoc)

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 