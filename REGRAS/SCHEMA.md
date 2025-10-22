-- Schema MariaDB - Nutri Xpert Pro (v2 - Escalável)
-- Este schema reflete uma estrutura de usuários unificada, que é uma prática recomendada para escalabilidade.

-- Tabela users (todos os tipos de usuário: admin, nutricionista, paciente)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(255) NOT NULL,  -- Criptografado
    last_login DATETIME(6) NULL,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    date_joined DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    user_type VARCHAR(20) NOT NULL CHECK (user_type IN ('admin', 'nutricionista', 'paciente'))
) COMMENT='Tabela unificada para todos os usuários que podem fazer login no sistema.';

-- Tabela de perfis de pacientes
CREATE TABLE patient_profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE NOT NULL, -- Link para o usuário paciente (One-to-One)
    nutritionist_id INT NOT NULL, -- Link para o usuário nutricionista
    birth_date DATE,
    phone VARCHAR(50),
    address TEXT,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (nutritionist_id) REFERENCES users(id) ON DELETE CASCADE
) COMMENT='Armazena informações de perfil específicas para usuários do tipo "paciente".';
CREATE INDEX idx_patient_profiles_user_id ON patient_profiles(user_id);
CREATE INDEX idx_patient_profiles_nutritionist_id ON patient_profiles(nutritionist_id);

-- Tabela diets
CREATE TABLE diets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_profile_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    meals JSON NOT NULL,
    substitutions JSON,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (patient_profile_id) REFERENCES patient_profiles(id) ON DELETE CASCADE
);
CREATE INDEX idx_diets_patient_profile_id ON diets(patient_profile_id);

-- Tabela anamneses
CREATE TABLE anamneses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_profile_id INT NOT NULL,
    weight DECIMAL(5,2),
    height DECIMAL(4,2),
    medical_conditions JSON,
    food_preferences JSON,
    allergies JSON,
    photo_url VARCHAR(500),
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (patient_profile_id) REFERENCES patient_profiles(id) ON DELETE CASCADE
);
CREATE INDEX idx_anamneses_patient_profile_id ON anamneses(patient_profile_id);

-- Tabela evaluations
CREATE TABLE evaluations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_profile_id INT NOT NULL,
    weight DECIMAL(5,2),
    body_measurements JSON,
    date DATETIME(6) NOT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (patient_profile_id) REFERENCES patient_profiles(id) ON DELETE CASCADE
);
CREATE INDEX idx_evaluations_patient_profile_id ON evaluations(patient_profile_id);

-- Tabela appointments
CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nutritionist_id INT NOT NULL, -- ID do nutricionista
    patient_profile_id INT NOT NULL,
    date DATETIME(6) NOT NULL,
    notes TEXT,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (nutritionist_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (patient_profile_id) REFERENCES patient_profiles(id) ON DELETE CASCADE
);
CREATE INDEX idx_appointments_nutritionist_id ON appointments(nutritionist_id);
CREATE INDEX idx_appointments_patient_profile_id ON appointments(patient_profile_id);

-- Tabela payments
CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL, -- ID do nutricionista que paga
    asaas_id VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE INDEX idx_payments_user_id ON payments(user_id);

-- Tabela notifications
CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL, -- Para qual usuário é a notificação
    type VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    sent_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);