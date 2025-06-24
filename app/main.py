from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.atleta import Base, Atleta
from app.database import engine, SessionLocal
from app.schemas.atleta_schema import AtletaCreate, AtletaResponse


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/atletas/", response_model=AtletaResponse)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    db_atleta = Atleta(**atleta.dict())
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

@app.get("/atletas/", response_model=list[AtletaResponse])
def listar_atletas(db: Session = Depends(get_db)):
    return db.query(Atleta).all()

@app.get("/atletas/{atleta_id}", response_model=AtletaResponse)
def buscar_atleta(atleta_id: int, db: Session = Depends(get_db)):
    atleta = db.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return atleta

@app.delete("/atletas/{atleta_id}")
def deletar_atleta(atleta_id: int, db: Session = Depends(get_db)):
    atleta = db.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    db.delete(atleta)
    db.commit()
    return {"mensagem": "Atleta deletado com sucesso"}
