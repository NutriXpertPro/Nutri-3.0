-- Schema PostgreSQL - Nutri Xpert Pro
-- Rode isso em um banco PostgreSQL vazio para criar as tabelas.

-- Tabela users (nutricionistas)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- Criptografado (use bcrypt ou similar)
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);

-- Tabela patients
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    birth_date DATE,
    phone VARCHAR(50),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX idx_patients_user_id ON patients(user_id);

-- Tabela diets
CREATE TABLE diets (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    meals JSONB NOT NULL,  -- Ex: [{"id": 1, "time": "08:00", "items": ["ovos", "abacate"]}, ...]
    substitutions JSONB,   -- Ex: {"frango": ["peixe", "tofu"]}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_patient_id FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE INDEX idx_diets_patient_id ON diets(patient_id);

-- Tabela anamneses
CREATE TABLE anamneses (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    weight DECIMAL(5,2),
    height DECIMAL(4,2),
    medical_conditions JSONB,  -- Ex: ["diabetes", "hipertensão"]
    food_preferences JSONB,
    allergies JSONB,
    photo_url VARCHAR(500),    -- Via AWS S3
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_patient_id FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE INDEX idx_anamneses_patient_id ON anamneses(patient_id);

-- Tabela evaluations
CREATE TABLE evaluations (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    weight DECIMAL(5,2),
    body_measurements JSONB,   -- Ex: {"waist": 80, "hip": 100, "neck": 35}
    date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_patient_id FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE INDEX idx_evaluations_patient_id ON evaluations(patient_id);

-- Tabela appointments
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    date TIMESTAMP NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_patient_id FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE INDEX idx_appointments_user_id ON appointments(user_id);
CREATE INDEX idx_appointments_patient_id ON appointments(patient_id);

-- Tabela payments
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    patient_id INTEGER REFERENCES patients(id) ON DELETE SET NULL,
    asaas_id VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) NOT NULL,  -- Ex: "PENDING", "PAID", "CANCELLED"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_patient_id FOREIGN KEY (patient_id) REFERENCES patients(id)
);
CREATE INDEX idx_payments_user_id ON payments(user_id);
CREATE INDEX idx_payments_patient_id ON payments(patient_id);

-- Tabela notifications
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL,   -- Ex: "email", "sms"
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);

-- Comentários para documentação (opcional)
COMMENT ON TABLE users IS 'Armazena nutricionistas';
COMMENT ON TABLE patients IS 'Armazena pacientes dos nutricionistas';
-- ... (adicione pros outros se quiser)