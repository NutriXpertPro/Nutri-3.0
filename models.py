from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Date,
    Text,
    ForeignKey,
    JSON,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    last_login = Column(DateTime, nullable=True)
    is_superuser = Column(Boolean, default=False, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    date_joined = Column(DateTime, default=func.now())
    user_type = Column(
        String(20), nullable=False
    )  # CHECK (user_type IN ('admin', 'nutricionista', 'paciente'))

    patient_profile = relationship(
        "PatientProfile", back_populates="user", uselist=False
    )
    nutritionist_patients = relationship(
        "PatientProfile",
        back_populates="nutritionist",
        foreign_keys="[PatientProfile.nutritionist_id]",
    )


class PatientProfile(Base):
    __tablename__ = "patient_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    nutritionist_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    birth_date = Column(Date, nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())

    user = relationship(
        "User", back_populates="patient_profile", foreign_keys=[user_id]
    )
    nutritionist = relationship(
        "User",
        back_populates="nutritionist_patients",
        foreign_keys=[nutritionist_id],
    )


# NOTA: As tabelas abaixo precisam ser ajustadas para refletir a nova estrutura.
# O campo `patient_id` deve ser substituído por `patient_profile_id` ou um link direto para `users(id)` do paciente.


class Diet(Base):
    __tablename__ = "diets"

    id = Column(Integer, primary_key=True, index=True)
    patient_profile_id = Column(
        Integer, ForeignKey("patient_profiles.id"), nullable=False
    )
    name = Column(String(255), nullable=False)
    meals = Column(JSON, nullable=False)  # Mapeado de JSONB para JSON para MariaDB
    substitutions = Column(
        JSON, nullable=True
    )  # Mapeado de JSONB para JSON para MariaDB
    created_at = Column(DateTime, default=func.now())

    patient_profile = relationship("PatientProfile")


class Anamnesis(Base):
    __tablename__ = "anamneses"

    id = Column(Integer, primary_key=True, index=True)
    patient_profile_id = Column(
        Integer, ForeignKey("patient_profiles.id"), nullable=False
    )  # MUDAR para patient_profile_id
    weight = Column(Text, nullable=True)  # DECIMAL(5,2)
    height = Column(Text, nullable=True)  # DECIMAL(4,2)
    medical_conditions = Column(
        JSON, nullable=True
    )  # Mapeado de JSONB para JSON para MariaDB
    food_preferences = Column(
        JSON, nullable=True
    )  # Mapeado de JSONB para JSON para MariaDB
    allergies = Column(JSON, nullable=True)  # Mapeado de JSONB para JSON para MariaDB
    photo_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=func.now())

    patient_profile = relationship("PatientProfile")


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    patient_profile_id = Column(
        Integer, ForeignKey("patient_profiles.id"), nullable=False
    )  # MUDAR para patient_profile_id
    weight = Column(Text, nullable=True)  # DECIMAL(5,2)
    body_measurements = Column(
        JSON, nullable=True
    )  # Mapeado de JSONB para JSON para MariaDB
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now())

    patient_profile = relationship("PatientProfile")


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    nutritionist_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # Este deve ser o ID do nutricionista
    patient_profile_id = Column(
        Integer, ForeignKey("patient_profiles.id"), nullable=False
    )  # MUDAR para patient_profile_id
    date = Column(DateTime, nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())

    nutritionist = relationship("User", foreign_keys=[nutritionist_id])
    patient_profile = relationship("PatientProfile")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # Este pode ser o nutricionista ou o paciente
    asaas_id = Column(String(255), nullable=False)
    amount = Column(Text, nullable=False)  # DECIMAL(10,2)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

    user = relationship("User")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # Para qual usuário é a notificação?
    type = Column(String(50), nullable=False)
    message = Column(Text, nullable=False)
    sent_at = Column(DateTime, default=func.now())

    user = relationship("User")
