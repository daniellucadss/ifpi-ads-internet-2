from pydantic import BaseModel

class ModeloBase(BaseModel):
    nome: str
    montadora_id: int
    valor_referencia: float
    ano_modelo: int
    motorizacao: float
    turbo: bool
    automatico: bool

class ModeloCreate(ModeloBase):
    pass

class ModeloUpdate(ModeloBase):
    pass

class Modelo(ModeloBase):
    id: int
    class Config:
        orm_mode = True