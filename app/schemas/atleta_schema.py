from pydantic import BaseModel

class AtletaBase(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str | None = None
    categoria: str | None = None

class AtletaCreate(AtletaBase):
    pass

class AtletaResponse(AtletaBase):
    id: int

    class Config:
        orm_mode = True
