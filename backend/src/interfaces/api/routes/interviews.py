from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.domain.schemas import Interview, InterviewCreate, InterviewUpdate
from src.application.services import InterviewService
from src.infrastructure.database import get_db

router = APIRouter(
    prefix="/interviews",
    tags=["interviews"],
    responses={404: {"description": "No encontrado"}},
)

interview_service = InterviewService()

@router.get("/", response_model=List[Interview])
def get_interviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtener todas las entrevistas.
    """
    interviews = interview_service.get_interviews(db, skip=skip, limit=limit)
    return interviews

@router.get("/{interview_id}", response_model=Interview)
def get_interview(interview_id: int, db: Session = Depends(get_db)):
    """
    Obtener una entrevista por su ID.
    """
    interview = interview_service.get_interview_by_id(db, interview_id=interview_id)
    if interview is None:
        raise HTTPException(status_code=404, detail="Entrevista no encontrada")
    return interview

@router.get("/application/{application_id}", response_model=List[Interview])
def get_interviews_by_application(application_id: int, db: Session = Depends(get_db)):
    """
    Obtener todas las entrevistas para una aplicación.
    """
    interviews = interview_service.get_interviews_by_application_id(db, application_id=application_id)
    return interviews

@router.post("/", response_model=Interview, status_code=status.HTTP_201_CREATED)
def create_interview(interview: InterviewCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva entrevista.
    """
    db_interview = interview_service.create_interview(db=db, interview_data=interview)
    if db_interview is None:
        raise HTTPException(
            status_code=400,
            detail="Aplicación no encontrada"
        )
    return db_interview

@router.put("/{interview_id}", response_model=Interview)
def update_interview(interview_id: int, interview: InterviewUpdate, db: Session = Depends(get_db)):
    """
    Actualizar una entrevista existente.
    """
    db_interview = interview_service.update_interview(db, interview_id=interview_id, interview_data=interview)
    if db_interview is None:
        raise HTTPException(status_code=404, detail="Entrevista no encontrada")
    return db_interview

@router.delete("/{interview_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interview(interview_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una entrevista.
    """
    success = interview_service.delete_interview(db, interview_id=interview_id)
    if not success:
        raise HTTPException(status_code=404, detail="Entrevista no encontrada")
    return None 