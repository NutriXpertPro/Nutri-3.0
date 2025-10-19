-- Schema PostgreSQL - Nutri Xpert Pro (v2 - Escalável)
-- Este schema reflete uma estrutura de usuários unificada, que é uma prática recomendada para escalabilidade.

-- Tabela users (todos os tipos de usuário: admin, nutricionista, paciente)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,  -- Criptografado
    last_login TIMESTAMP,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_type VARCHAR(20) NOT NULL CHECK (user_type IN ('admin', 'nutricionista', 'paciente'))
);
COMMENT ON TABLE users IS 'Tabela unificada para todos os usuários que podem fazer login no sistema.';

-- Tabela de perfis de pacientes
CREATE TABLE patient_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Link para o usuário paciente (One-to-One)
    nutritionist_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Link para o usuário nutricionista
    birth_date DATE,
    phone VARCHAR(50),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- O nome e email do paciente agora residem na tabela `users`.
    -- Outros campos específicos do paciente podem ser adicionados aqui.
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_nutritionist FOREIGN KEY (nutritionist_id) REFERENCES users(id)
);
COMMENT ON TABLE patient_profiles IS 'Armazena informações de perfil específicas para usuários do tipo "paciente".';
CREATE INDEX idx_patient_profiles_user_id ON patient_profiles(user_id);
CREATE INDEX idx_patient_profiles_nutritionist_id ON patient_profiles(nutritionist_id);


-- NOTA: As tabelas abaixo precisam ser ajustadas para refletir a nova estrutura.
-- O campo `patient_id` deve ser substituído por `patient_profile_id` ou um link direto para `users(id)` do paciente.

-- Tabela diets (Exemplo de como ficaria)
CREATE TABLE diets (
    id SERIAL PRIMARY KEY,
    patient_profile_id INTEGER NOT NULL REFERENCES patient_profiles(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    meals JSONB NOT NULL,
    substitutions JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_patient_profile FOREIGN KEY (patient_profile_id) REFERENCES patient_profiles(id)
);
CREATE INDEX idx_diets_patient_profile_id ON diets(patient_profile_id);


-- Tabela anamneses (A ser ajustada)
CREATE TABLE anamneses (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL, -- MUDAR para patient_profile_id
    weight DECIMAL(5,2),
    height DECIMAL(4,2),
    medical_conditions JSONB,
    food_preferences JSONB,
    allergies JSONB,
    photo_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela evaluations (A ser ajustada)
CREATE TABLE evaluations (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL, -- MUDAR para patient_profile_id
    weight DECIMAL(5,2),
    body_measurements JSONB,
    date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela appointments (A ser ajustada)
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL, -- Este deve ser o ID do nutricionista
    patient_id INTEGER NOT NULL, -- MUDAR para patient_profile_id
    date TIMESTAMP NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela payments (A ser ajustada)
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL, -- Este pode ser o nutricionista ou o paciente
    asaas_id VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela notifications (A ser ajustada)
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL, -- Para qual usuário é a notificação?
    type VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
