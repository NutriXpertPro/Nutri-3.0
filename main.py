from fastapi import FastAPI, Depends, HTTPException

app = FastAPI(
    title="Nutri Xpert Pro API",
    description="API para gerenciamento nutricional",
    version="3.0",
)

@app.get("/")
def read_root():
    """
    Endpoint raiz da API
    """
    return {
        "message": "Bem-vindo ao Nutri Xpert Pro API!",
        "version": "3.0",
        "docs": "/docs",
    }


@app.get("/healthcheck")
def healthcheck():
    """
    Verifica se a API está funcionando
    """
    return {
        "status": "ok",
        "message": "API is running",
    }

@app.get("/database/info")
def database_info():
    """
    Retorna informações sobre o banco de dados (apenas placeholder, sem acesso direto)
    """
    return {
        "message": "Database access removed from FastAPI. Use Django for database operations.",
        "status": "info_unavailable",
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
