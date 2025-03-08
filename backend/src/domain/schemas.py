from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, HttpUrl

# Esquemas para Candidate
class CandidateBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    resume_url: Optional[str] = None
    linkedin_url: Optional[str] = None

class CandidateCreate(CandidateBase):
    pass

class CandidateUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    resume_url: Optional[str] = None
    linkedin_url: Optional[str] = None

class Candidate(CandidateBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Esquemas para JobPosition
class JobPositionBase(BaseModel):
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None
    salary_range: Optional[str] = None
    is_active: bool = True

class JobPositionCreate(JobPositionBase):
    pass

class JobPositionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None
    salary_range: Optional[str] = None
    is_active: Optional[bool] = None

class JobPosition(JobPositionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Esquemas para Application
class ApplicationBase(BaseModel):
    candidate_id: int
    job_position_id: int
    status: str = "applied"
    notes: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

class Application(ApplicationBase):
    id: int
    application_date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Esquemas para Interview
class InterviewBase(BaseModel):
    application_id: int
    interviewer_name: str
    interview_date: datetime
    feedback: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    status: str = "scheduled"

class InterviewCreate(InterviewBase):
    pass

class InterviewUpdate(BaseModel):
    interviewer_name: Optional[str] = None
    interview_date: Optional[datetime] = None
    feedback: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    status: Optional[str] = None

class Interview(InterviewBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 