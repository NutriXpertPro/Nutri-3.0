from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, engine, Base, get_db

# Importar todos os models para que o SQLAlchemy os reconheça
import models

app = FastAPI(
    title="Nutri Xpert Pro API",
    description="API para gerenciamento nutricional",
    version="3.0"
)

# Criar todas as tabelas no banco de dados
print("--- Criando tabelas no banco de dados ---")
Base.metadata.create_all(bind=engine)
print("--- Tabelas criadas com sucesso! ---")


@app.get("/")
def read_root():
    """
    Endpoint raiz da API
    """
    return {
        "message": "Bem-vindo ao Nutri Xpert Pro API!",
        "version": "3.0",
        "docs": "/docs"
    }


@app.get("/healthcheck")
def healthcheck(db: Session = Depends(get_db)):
    """
    Verifica se a API e o banco de dados estão funcionando
    """
    try:
        # Testa a conexão com o banco
        db.execute(text("SELECT 1"))
        
        # Conta quantas tabelas existem
        result = db.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]
        
        return {
            "status": "ok",
            "database": "connected",
            "database_name": "nutri_db",
            "tables_count": len(tables),
            "tables": tables
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )


@app.get("/database/info")
def database_info(db: Session = Depends(get_db)):
    """
    Retorna informações sobre o banco de dados
    """
    try:
        # Versão do MariaDB
        version_result = db.execute(text("SELECT VERSION()"))
        version = version_result.fetchone()[0]
        
        # Nome do banco atual
        db_result = db.execute(text("SELECT DATABASE()"))
        database_name = db_result.fetchone()[0]
        
        # Listar todas as tabelas
        tables_result = db.execute(text("SHOW TABLES"))
        tables = [row[0] for row in tables_result]
        
        return {
            "mariadb_version": version,
            "database_name": database_name,
            "tables": tables,
            "total_tables": len(tables)
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get database info: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)