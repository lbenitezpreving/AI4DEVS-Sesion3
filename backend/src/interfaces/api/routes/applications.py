from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.domain.schemas import Application, ApplicationCreate, ApplicationUpdate
from src.application.services import ApplicationService
from src.infrastructure.database import get_db

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
    responses={404: {"description": "No encontrado"}},
)

application_service = ApplicationService()

@router.get("/", response_model=List[Application])
def get_applications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtener todas las aplicaciones.
    """
    applications = application_service.get_applications(db, skip=skip, limit=limit)
    return applications

@router.get("/{application_id}", response_model=Application)
def get_application(application_id: int, db: Session = Depends(get_db)):
    """
    Obtener una aplicación por su ID.
    """
    application = application_service.get_application_by_id(db, application_id=application_id)
    if application is None:
        raise HTTPException(status_code=404, detail="Aplicación no encontrada")
    return application

@router.get("/candidate/{candidate_id}", response_model=List[Application])
def get_applications_by_candidate(candidate_id: int, db: Session = Depends(get_db)):
    """
    Obtener todas las aplicaciones de un candidato.
    """
    applications = application_service.get_applications_by_candidate_id(db, candidate_id=candidate_id)
    return applications

@router.get("/job-position/{job_position_id}", response_model=List[Application])
def get_applications_by_job_position(job_position_id: int, db: Session = Depends(get_db)):
    """
    Obtener todas las aplicaciones para una posición de trabajo.
    """
    applications = application_service.get_applications_by_job_position_id(db, job_position_id=job_position_id)
    return applications

@router.post("/", response_model=Application, status_code=status.HTTP_201_CREATED)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva aplicación.
    """
    db_application = application_service.create_application(db=db, application_data=application)
    if db_application is None:
        raise HTTPException(
            status_code=400,
            detail="Candidato o posición de trabajo no encontrados"
        )
    return db_application

@router.put("/{application_id}", response_model=Application)
def update_application(application_id: int, application: ApplicationUpdate, db: Session = Depends(get_db)):
    """
    Actualizar una aplicación existente.
    """
    db_application = application_service.update_application(db, application_id=application_id, application_data=application)
    if db_application is None:
        raise HTTPException(status_code=404, detail="Aplicación no encontrada")
    return db_application

@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una aplicación.
    """
    success = application_service.delete_application(db, application_id=application_id)
    if not success:
        raise HTTPException(status_code=404, detail="Aplicación no encontrada")
    return None 