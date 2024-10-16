from pydantic import BaseModel

class MontadoraBase(BaseModel):
    nome: str
    pais: str
    ano_fundacao: int

class MontadoraCreate(MontadoraBase):
    pass

class MontadoraUpdate(MontadoraBase):
    pass

class Montadora(MontadoraBase):
    id: int
    class Config:
        orm_mode = True