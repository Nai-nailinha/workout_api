from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.atleta import Base, Atleta
from app.database import engine, SessionLocal
from app.routes import atleta_route  # importa o roteador

app = FastAPI()

# Inclui as rotas definidas no atleta_route.py
#app.include_router(atleta_route.router)
print("Conteúdo atleta_route:", dir(atleta_route))


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota inicial da API (opcional, mas simpática)
@app.get("/")
def read_root():
    return {"message": "Bem-vinda à Workout API 🚴‍♀️💪"}

