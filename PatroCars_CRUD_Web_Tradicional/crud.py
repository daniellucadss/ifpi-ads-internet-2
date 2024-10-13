from sqlmodel import select, Session
from models import Carro, Montadora
from schemas import CarroCreate, MontadoraCreate

def get_montadoras(db: Session):
    # return db.exec(select(Montadora).offset(skip).limit(limit)).all()
    montadoras = db.exec(select(Montadora)).all()
    return montadoras

def get_montadora(db: Session, montadora_id: int):
    montadora = db.exec(select(Montadora).where(Montadora.id == montadora_id)).first()
    return montadora

def create_montadora(db: Session, montadora: MontadoraCreate):
    db_montadora = Montadora(nome=montadora.nome, pais=montadora.pais, ano_fundacao=montadora.ano_fundacao)
    db.add(db_montadora)
    db.commit()
    db.refresh(db_montadora)    
    return db_montadora

def get_carros(db: Session):
    carros = db.exec(select(Carro)).all()
    return carros

def get_carro(db: Session, carro_id: int):
    carro = db.exec(select(Carro).where(Carro.id == carro_id)).first()
    if carro:
        montadora = db.exec(select(Montadora).where(Montadora.id == carro.montadora_id)).first()
        carro.montadora = montadora 
    return carro

def get_carro(db: Session, carro_id: int):
    carro = db.exec(select(Carro).where(Carro.id == carro_id)).first()
    print(carro)
    if carro:
        montadora = db.exec(select(Montadora).where(Montadora.id == carro.montadora_id)).first()
        carro.montadora = montadora if montadora else None
    return carro

def create_carro(db: Session, carro: CarroCreate):
    db_carro = Carro(nome=carro.nome, ano_fabricacao=carro.ano_fabricacao, montadora_id=carro.montadora_id)
    db.add(db_carro)
    db.commit()
    db.refresh(db_carro)    
    return db_carro