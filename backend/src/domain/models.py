from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.infrastructure.database import Base

class Candidate(Base):
    __tablename__ = "candidates"
    __table_args__ = {"schema": "ats"}

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(50))
    resume_url = Column(Text)
    linkedin_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="candidate")

class JobPosition(Base):
    __tablename__ = "job_positions"
    __table_args__ = {"schema": "ats"}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    requirements = Column(Text)
    department = Column(String(100))
    location = Column(String(100))
    salary_range = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="job_position")

class Application(Base):
    __tablename__ = "applications"
    __table_args__ = {"schema": "ats"}

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("ats.candidates.id"))
    job_position_id = Column(Integer, ForeignKey("ats.job_positions.id"))
    status = Column(String(50), default="applied", index=True)
    application_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    candidate = relationship("Candidate", back_populates="applications")
    job_position = relationship("JobPosition", back_populates="applications")
    interviews = relationship("Interview", back_populates="application")

class Interview(Base):
    __tablename__ = "interviews"
    __table_args__ = {"schema": "ats"}

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("ats.applications.id"))
    interviewer_name = Column(String(200))
    interview_date = Column(DateTime)
    feedback = Column(Text)
    rating = Column(Integer)
    status = Column(String(50), default="scheduled")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    application = relationship("Application", back_populates="interviews") 