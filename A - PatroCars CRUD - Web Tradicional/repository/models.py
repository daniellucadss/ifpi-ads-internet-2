from typing import List
from sqlmodel import Field, Relationship, SQLModel

class Usuario(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  username: str = Field(index=True, unique=True)
  password: str

class Montadora(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome: str
  pais: str
  ano_fundacao: int
  modelos: List["Modelo"] = Relationship(back_populates="montadora")

class Modelo(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome: str
  montadora_id: int = Field(foreign_key="montadora.id")
  valor_referencia: float
  ano_modelo: int
  motorizacao: float
  turbo: bool
  automatico: bool
  montadora: Montadora = Relationship(back_populates="modelos")
  veiculos: List["Veiculo"] = Relationship(back_populates="modelo")

class Veiculo(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  modelo_id: int = Field(foreign_key="modelo.id")
  cor: str
  ano_fabricacao: int
  valor: int
  placa: str
  vendido: bool
  modelo: Modelo = Relationship(back_populates="veiculos")