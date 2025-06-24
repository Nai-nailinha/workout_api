from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.atleta import Atleta
from app.schemas.atleta_schema import AtletaCreate, AtletaResponse
from app.database import get_db
from fastapi import Query

router = APIRouter()




@router.get("/atletas", response_model=list[AtletaResponse])
def get_all_atletas(
    nome: str | None = None,
    cpf: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Atleta)
    
    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)

    return query.all()


@router.post("/atletas", response_model=AtletaResponse)
def create_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo_atleta = Atleta(**atleta.dict())
    db.add(novo_atleta)
    db.commit()
    db.refresh(novo_atleta)
    return novo_atleta

