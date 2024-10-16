from pydantic import BaseModel

class VeiculoBase(BaseModel):
    modelo_id: int
    cor: str
    ano_fabricacao: int
    valor: int
    placa: str
    vendido: bool

class VeiculoCreate(VeiculoBase):
    pass

class VeiculoUpdate(VeiculoBase):
    pass

class Veiculo(VeiculoBase):
    id: int
    class Config:
        orm_mode = True