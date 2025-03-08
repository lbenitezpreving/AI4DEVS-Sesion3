from typing import List, Optional
from sqlalchemy.orm import Session

from src.domain.models import Candidate, JobPosition, Application, Interview

# Repositorio para Candidate
class CandidateRepository:
    def get_candidates(self, db: Session, skip: int = 0, limit: int = 100) -> List[Candidate]:
        return db.query(Candidate).offset(skip).limit(limit).all()

    def get_candidate_by_id(self, db: Session, candidate_id: int) -> Optional[Candidate]:
        return db.query(Candidate).filter(Candidate.id == candidate_id).first()

    def get_candidate_by_email(self, db: Session, email: str) -> Optional[Candidate]:
        return db.query(Candidate).filter(Candidate.email == email).first()

    def create_candidate(self, db: Session, candidate: Candidate) -> Candidate:
        db.add(candidate)
        db.commit()
        db.refresh(candidate)
        return candidate

    def update_candidate(self, db: Session, candidate: Candidate) -> Candidate:
        db.commit()
        db.refresh(candidate)
        return candidate

    def delete_candidate(self, db: Session, candidate: Candidate) -> None:
        db.delete(candidate)
        db.commit()

# Repositorio para JobPosition
class JobPositionRepository:
    def get_job_positions(self, db: Session, skip: int = 0, limit: int = 100) -> List[JobPosition]:
        return db.query(JobPosition).offset(skip).limit(limit).all()

    def get_active_job_positions(self, db: Session, skip: int = 0, limit: int = 100) -> List[JobPosition]:
        return db.query(JobPosition).filter(JobPosition.is_active == True).offset(skip).limit(limit).all()

    def get_job_position_by_id(self, db: Session, job_position_id: int) -> Optional[JobPosition]:
        return db.query(JobPosition).filter(JobPosition.id == job_position_id).first()

    def create_job_position(self, db: Session, job_position: JobPosition) -> JobPosition:
        db.add(job_position)
        db.commit()
        db.refresh(job_position)
        return job_position

    def update_job_position(self, db: Session, job_position: JobPosition) -> JobPosition:
        db.commit()
        db.refresh(job_position)
        return job_position

    def delete_job_position(self, db: Session, job_position: JobPosition) -> None:
        db.delete(job_position)
        db.commit()

# Repositorio para Application
class ApplicationRepository:
    def get_applications(self, db: Session, skip: int = 0, limit: int = 100) -> List[Application]:
        return db.query(Application).offset(skip).limit(limit).all()

    def get_application_by_id(self, db: Session, application_id: int) -> Optional[Application]:
        return db.query(Application).filter(Application.id == application_id).first()

    def get_applications_by_candidate_id(self, db: Session, candidate_id: int) -> List[Application]:
        return db.query(Application).filter(Application.candidate_id == candidate_id).all()

    def get_applications_by_job_position_id(self, db: Session, job_position_id: int) -> List[Application]:
        return db.query(Application).filter(Application.job_position_id == job_position_id).all()

    def create_application(self, db: Session, application: Application) -> Application:
        db.add(application)
        db.commit()
        db.refresh(application)
        return application

    def update_application(self, db: Session, application: Application) -> Application:
        db.commit()
        db.refresh(application)
        return application

    def delete_application(self, db: Session, application: Application) -> None:
        db.delete(application)
        db.commit()

# Repositorio para Interview
class InterviewRepository:
    def get_interviews(self, db: Session, skip: int = 0, limit: int = 100) -> List[Interview]:
        return db.query(Interview).offset(skip).limit(limit).all()

    def get_interview_by_id(self, db: Session, interview_id: int) -> Optional[Interview]:
        return db.query(Interview).filter(Interview.id == interview_id).first()

    def get_interviews_by_application_id(self, db: Session, application_id: int) -> List[Interview]:
        return db.query(Interview).filter(Interview.application_id == application_id).all()

    def create_interview(self, db: Session, interview: Interview) -> Interview:
        db.add(interview)
        db.commit()
        db.refresh(interview)
        return interview

    def update_interview(self, db: Session, interview: Interview) -> Interview:
        db.commit()
        db.refresh(interview)
        return interview

    def delete_interview(self, db: Session, interview: Interview) -> None:
        db.delete(interview)
        db.commit() 