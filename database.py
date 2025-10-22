import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

print("--- DEBUG: Loading database.py (unique identifier) ---")

# Load environment variables from .env file
load_dotenv()

# Get DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if DATABASE_URL is set and override to SQLite for local dev (no MySQL needed)
if not DATABASE_URL or "mysql" in DATABASE_URL.lower():
    DATABASE_URL = "sqlite:///./db.sqlite3"
    print("--- DEBUG: Overrode to SQLite for local development ---")

# Check if DATABASE_URL is now set
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")

engine = create_engine(
    DATABASE_URL, pool_size=20, max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()