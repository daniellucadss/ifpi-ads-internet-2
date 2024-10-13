from pydantic import BaseModel

class MontadoraBase(BaseModel):
    nome: str
    pais: str
    ano_fundacao: int

class MontadoraCreate(MontadoraBase):
    pass

class Montadora(MontadoraBase):
    id: int
    class Config:
        orm_mode = True

class CarroBase(BaseModel):
    nome: str
    ano_fabricacao: int
    montadora_id: int

class CarroCreate(CarroBase):
    pass

class Carro(CarroBase):
    id: int
    class Config:
        orm_mode = True
