from typing import List, Optional
from sqlalchemy.orm import Session

from src.domain.models import Candidate, JobPosition, Application, Interview
from src.domain.schemas import CandidateCreate, CandidateUpdate, JobPositionCreate, JobPositionUpdate, ApplicationCreate, ApplicationUpdate, InterviewCreate, InterviewUpdate
from src.application.repositories import CandidateRepository, JobPositionRepository, ApplicationRepository, InterviewRepository

# Servicio para Candidate
class CandidateService:
    def __init__(self):
        self.repository = CandidateRepository()

    def get_candidates(self, db: Session, skip: int = 0, limit: int = 100) -> List[Candidate]:
        return self.repository.get_candidates(db, skip, limit)

    def get_candidate_by_id(self, db: Session, candidate_id: int) -> Optional[Candidate]:
        return self.repository.get_candidate_by_id(db, candidate_id)

    def get_candidate_by_email(self, db: Session, email: str) -> Optional[Candidate]:
        return self.repository.get_candidate_by_email(db, email)

    def create_candidate(self, db: Session, candidate_data: CandidateCreate) -> Candidate:
        candidate = Candidate(**candidate_data.dict())
        return self.repository.create_candidate(db, candidate)

    def update_candidate(self, db: Session, candidate_id: int, candidate_data: CandidateUpdate) -> Optional[Candidate]:
        candidate = self.repository.get_candidate_by_id(db, candidate_id)
        if not candidate:
            return None
        
        for key, value in candidate_data.dict(exclude_unset=True).items():
            setattr(candidate, key, value)
        
        return self.repository.update_candidate(db, candidate)

    def delete_candidate(self, db: Session, candidate_id: int) -> bool:
        candidate = self.repository.get_candidate_by_id(db, candidate_id)
        if not candidate:
            return False
        
        self.repository.delete_candidate(db, candidate)
        return True

# Servicio para JobPosition
class JobPositionService:
    def __init__(self):
        self.repository = JobPositionRepository()

    def get_job_positions(self, db: Session, skip: int = 0, limit: int = 100) -> List[JobPosition]:
        return self.repository.get_job_positions(db, skip, limit)

    def get_active_job_positions(self, db: Session, skip: int = 0, limit: int = 100) -> List[JobPosition]:
        return self.repository.get_active_job_positions(db, skip, limit)

    def get_job_position_by_id(self, db: Session, job_position_id: int) -> Optional[JobPosition]:
        return self.repository.get_job_position_by_id(db, job_position_id)

    def create_job_position(self, db: Session, job_position_data: JobPositionCreate) -> JobPosition:
        job_position = JobPosition(**job_position_data.dict())
        return self.repository.create_job_position(db, job_position)

    def update_job_position(self, db: Session, job_position_id: int, job_position_data: JobPositionUpdate) -> Optional[JobPosition]:
        job_position = self.repository.get_job_position_by_id(db, job_position_id)
        if not job_position:
            return None
        
        for key, value in job_position_data.dict(exclude_unset=True).items():
            setattr(job_position, key, value)
        
        return self.repository.update_job_position(db, job_position)

    def delete_job_position(self, db: Session, job_position_id: int) -> bool:
        job_position = self.repository.get_job_position_by_id(db, job_position_id)
        if not job_position:
            return False
        
        self.repository.delete_job_position(db, job_position)
        return True

# Servicio para Application
class ApplicationService:
    def __init__(self):
        self.repository = ApplicationRepository()
        self.candidate_repository = CandidateRepository()
        self.job_position_repository = JobPositionRepository()

    def get_applications(self, db: Session, skip: int = 0, limit: int = 100) -> List[Application]:
        return self.repository.get_applications(db, skip, limit)

    def get_application_by_id(self, db: Session, application_id: int) -> Optional[Application]:
        return self.repository.get_application_by_id(db, application_id)

    def get_applications_by_candidate_id(self, db: Session, candidate_id: int) -> List[Application]:
        return self.repository.get_applications_by_candidate_id(db, candidate_id)

    def get_applications_by_job_position_id(self, db: Session, job_position_id: int) -> List[Application]:
        return self.repository.get_applications_by_job_position_id(db, job_position_id)

    def create_application(self, db: Session, application_data: ApplicationCreate) -> Optional[Application]:
        # Verificar que el candidato existe
        candidate = self.candidate_repository.get_candidate_by_id(db, application_data.candidate_id)
        if not candidate:
            return None
        
        # Verificar que la posición de trabajo existe
        job_position = self.job_position_repository.get_job_position_by_id(db, application_data.job_position_id)
        if not job_position:
            return None
        
        application = Application(**application_data.dict())
        return self.repository.create_application(db, application)

    def update_application(self, db: Session, application_id: int, application_data: ApplicationUpdate) -> Optional[Application]:
        application = self.repository.get_application_by_id(db, application_id)
        if not application:
            return None
        
        for key, value in application_data.dict(exclude_unset=True).items():
            setattr(application, key, value)
        
        return self.repository.update_application(db, application)

    def delete_application(self, db: Session, application_id: int) -> bool:
        application = self.repository.get_application_by_id(db, application_id)
        if not application:
            return False
        
        self.repository.delete_application(db, application)
        return True

# Servicio para Interview
class InterviewService:
    def __init__(self):
        self.repository = InterviewRepository()
        self.application_repository = ApplicationRepository()

    def get_interviews(self, db: Session, skip: int = 0, limit: int = 100) -> List[Interview]:
        return self.repository.get_interviews(db, skip, limit)

    def get_interview_by_id(self, db: Session, interview_id: int) -> Optional[Interview]:
        return self.repository.get_interview_by_id(db, interview_id)

    def get_interviews_by_application_id(self, db: Session, application_id: int) -> List[Interview]:
        return self.repository.get_interviews_by_application_id(db, application_id)

    def create_interview(self, db: Session, interview_data: InterviewCreate) -> Optional[Interview]:
        # Verificar que la aplicación existe
        application = self.application_repository.get_application_by_id(db, interview_data.application_id)
        if not application:
            return None
        
        interview = Interview(**interview_data.dict())
        return self.repository.create_interview(db, interview)

    def update_interview(self, db: Session, interview_id: int, interview_data: InterviewUpdate) -> Optional[Interview]:
        interview = self.repository.get_interview_by_id(db, interview_id)
        if not interview:
            return None
        
        for key, value in interview_data.dict(exclude_unset=True).items():
            setattr(interview, key, value)
        
        return self.repository.update_interview(db, interview)

    def delete_interview(self, db: Session, interview_id: int) -> bool:
        interview = self.repository.get_interview_by_id(db, interview_id)
        if not interview:
            return False
        
        self.repository.delete_interview(db, interview)
        return True 