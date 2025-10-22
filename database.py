import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

print("--- Carregando configuração do banco de dados ---")

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter DATABASE_URL das variáveis de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não está definida no arquivo .env")

print(f"--- Conectando ao banco: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else 'local'} ---")

# Criar engine do SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verifica conexão antes de usar
    pool_recycle=3600,   # Recicla conexões a cada hora
    echo=False           # Mude para True para ver as queries SQL no console
)

# Criar SessionLocal para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()

# Dependency para FastAPI
def get_db():
    """
    Cria uma sessão do banco de dados e garante que seja fechada após o uso
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()