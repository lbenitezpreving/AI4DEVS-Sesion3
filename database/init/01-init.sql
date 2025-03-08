-- Crear esquemas
CREATE SCHEMA IF NOT EXISTS ats;

-- Configurar permisos
GRANT ALL PRIVILEGES ON SCHEMA ats TO lti_admin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA ats TO lti_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA ats GRANT ALL PRIVILEGES ON TABLES TO lti_admin;

-- Crear tablas principales
CREATE TABLE IF NOT EXISTS ats.candidates (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    resume_url TEXT,
    linkedin_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ats.job_positions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    requirements TEXT,
    department VARCHAR(100),
    location VARCHAR(100),
    salary_range VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ats.applications (
    id SERIAL PRIMARY KEY,
    candidate_id INTEGER REFERENCES ats.candidates(id),
    job_position_id INTEGER REFERENCES ats.job_positions(id),
    status VARCHAR(50) DEFAULT 'applied',
    application_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ats.interviews (
    id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES ats.applications(id),
    interviewer_name VARCHAR(200),
    interview_date TIMESTAMP WITH TIME ZONE,
    feedback TEXT,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    status VARCHAR(50) DEFAULT 'scheduled',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Crear índices
CREATE INDEX idx_candidates_email ON ats.candidates(email);
CREATE INDEX idx_applications_candidate_id ON ats.applications(candidate_id);
CREATE INDEX idx_applications_job_position_id ON ats.applications(job_position_id);
CREATE INDEX idx_applications_status ON ats.applications(status);
CREATE INDEX idx_interviews_application_id ON ats.interviews(application_id);

-- Crear función para actualizar el timestamp de actualización
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Crear triggers para actualizar el timestamp de actualización
CREATE TRIGGER update_candidates_updated_at BEFORE UPDATE ON ats.candidates
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_job_positions_updated_at BEFORE UPDATE ON ats.job_positions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_applications_updated_at BEFORE UPDATE ON ats.applications
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_interviews_updated_at BEFORE UPDATE ON ats.interviews
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column(); 