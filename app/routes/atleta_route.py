from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.atleta import Atleta
from app.schemas.atleta_schema import AtletaCreate, AtletaResponse
from app.database import get_db
from fastapi import Query
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate
from fastapi_pagination.paginator import paginate
from fastapi_pagination import add_pagination
from typing import Optional



router = APIRouter()

@router.get("/atletas", response_model=Page[AtletaResponse])
def get_all_atletas(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None),
    cpf: Optional[str] = Query(None)
):
    query = db.query(Atleta)

    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)

    return paginate(query)


""" @router.get("/atletas", response_model=Page[AtletaResponse])
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

    return query.all() """


@router.post("/atletas", response_model=AtletaResponse)
def create_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo_atleta = Atleta(**atleta.dict())
    db.add(novo_atleta)
    try:
        db.commit()
        db.refresh(novo_atleta)
        return novo_atleta
    except IntegrityError as e:
        db.rollback()
        if "UNIQUE constraint" in str(e.orig) or "duplicate key" in str(e.orig):
            raise HTTPException(status_code=400, detail="CPF já cadastrado.")
        raise HTTPException(status_code=500, detail="Erro ao cadastrar atleta.")


