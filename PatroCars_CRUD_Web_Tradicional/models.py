from typing import List
from sqlmodel import Field, Relationship, SQLModel

class Carro(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome: str
  ano_fabricacao: int
  montadora_id: int = Field(foreign_key="montadora.id")
  montadora: "Montadora" = Relationship(back_populates="carros")
  
class Montadora(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome: str
  pais: str
  ano_fundacao: int
  carros: List[Carro] = Relationship(back_populates="montadora")