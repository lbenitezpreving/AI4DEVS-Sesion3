from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.domain.schemas import JobPosition, JobPositionCreate, JobPositionUpdate
from src.application.services import JobPositionService
from src.infrastructure.database import get_db

router = APIRouter(
    prefix="/job-positions",
    tags=["job_positions"],
    responses={404: {"description": "No encontrado"}},
)

job_position_service = JobPositionService()

@router.get("/", response_model=List[JobPosition])
def get_job_positions(skip: int = 0, limit: int = 100, active_only: bool = False, db: Session = Depends(get_db)):
    """
    Obtener todas las posiciones de trabajo.
    """
    if active_only:
        job_positions = job_position_service.get_active_job_positions(db, skip=skip, limit=limit)
    else:
        job_positions = job_position_service.get_job_positions(db, skip=skip, limit=limit)
    return job_positions

@router.get("/{job_position_id}", response_model=JobPosition)
def get_job_position(job_position_id: int, db: Session = Depends(get_db)):
    """
    Obtener una posición de trabajo por su ID.
    """
    job_position = job_position_service.get_job_position_by_id(db, job_position_id=job_position_id)
    if job_position is None:
        raise HTTPException(status_code=404, detail="Posición de trabajo no encontrada")
    return job_position

@router.post("/", response_model=JobPosition, status_code=status.HTTP_201_CREATED)
def create_job_position(job_position: JobPositionCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva posición de trabajo.
    """
    return job_position_service.create_job_position(db=db, job_position_data=job_position)

@router.put("/{job_position_id}", response_model=JobPosition)
def update_job_position(job_position_id: int, job_position: JobPositionUpdate, db: Session = Depends(get_db)):
    """
    Actualizar una posición de trabajo existente.
    """
    db_job_position = job_position_service.update_job_position(db, job_position_id=job_position_id, job_position_data=job_position)
    if db_job_position is None:
        raise HTTPException(status_code=404, detail="Posición de trabajo no encontrada")
    return db_job_position

@router.delete("/{job_position_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job_position(job_position_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una posición de trabajo.
    """
    success = job_position_service.delete_job_position(db, job_position_id=job_position_id)
    if not success:
        raise HTTPException(status_code=404, detail="Posición de trabajo no encontrada")
    return None 