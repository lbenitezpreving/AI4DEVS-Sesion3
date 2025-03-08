from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.domain.schemas import Candidate, CandidateCreate, CandidateUpdate
from src.application.services import CandidateService
from src.infrastructure.database import get_db

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={404: {"description": "No encontrado"}},
)

candidate_service = CandidateService()

@router.get("/", response_model=List[Candidate])
def get_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtener todos los candidatos.
    """
    candidates = candidate_service.get_candidates(db, skip=skip, limit=limit)
    return candidates

@router.get("/{candidate_id}", response_model=Candidate)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    """
    Obtener un candidato por su ID.
    """
    candidate = candidate_service.get_candidate_by_id(db, candidate_id=candidate_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return candidate

@router.post("/", response_model=Candidate, status_code=status.HTTP_201_CREATED)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    """
    Crear un nuevo candidato.
    """
    db_candidate = candidate_service.get_candidate_by_email(db, email=candidate.email)
    if db_candidate:
        raise HTTPException(
            status_code=400,
            detail="El email ya está registrado"
        )
    return candidate_service.create_candidate(db=db, candidate_data=candidate)

@router.put("/{candidate_id}", response_model=Candidate)
def update_candidate(candidate_id: int, candidate: CandidateUpdate, db: Session = Depends(get_db)):
    """
    Actualizar un candidato existente.
    """
    db_candidate = candidate_service.update_candidate(db, candidate_id=candidate_id, candidate_data=candidate)
    if db_candidate is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return db_candidate

@router.delete("/{candidate_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    """
    Eliminar un candidato.
    """
    success = candidate_service.delete_candidate(db, candidate_id=candidate_id)
    if not success:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return None 