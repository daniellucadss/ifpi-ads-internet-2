from sqlmodel import select, Session
from models import Carro, Montadora
from schemas import CarroCreate, CarroUpdate, MontadoraCreate, MontadoraUpdate

def create_montadora(db: Session, montadora: MontadoraCreate):
    db_montadora = Montadora()
    db_montadora.nome = montadora.nome
    db_montadora.pais = montadora.pais
    db_montadora.ano_fundacao = montadora.ano_fundacao
    db.add(db_montadora)
    db.commit()
    db.refresh(db_montadora)    
    return db_montadora

def get_montadoras(db: Session):
    montadoras = db.exec(select(Montadora).order_by(Montadora.id)).all()
    return montadoras

def get_montadora(db: Session, montadora_id: int):
    montadora = db.exec(select(Montadora).where(Montadora.id == montadora_id)).first()
    return montadora

def update_montadora(db: Session, montadora_id: int, montadora: MontadoraUpdate):
    db_montadora = get_montadora(db, montadora_id)
    db_montadora.nome = montadora.nome
    db_montadora.pais = montadora.pais
    db_montadora.ano_fundacao = montadora.ano_fundacao
    db.add(db_montadora)
    db.commit()
    db.refresh(db_montadora)
    return db_montadora

def delete_montadora(db: Session, montadora_id: int):
    db_montadora = get_montadora(db, montadora_id)
    db.delete(db_montadora)
    db.commit()

def create_carro(db: Session, carro: CarroCreate):
    db_carro = Carro()
    db_carro.nome=carro.nome, 
    db_carro.ano_fabricacao=carro.ano_fabricacao, 
    db_carro.montadora_id=carro.montadora_id
    db.add(db_carro)
    db.commit()
    db.refresh(db_carro)    
    return db_carro

def get_carros(db: Session):
    carros = db.exec(select(Carro).order_by(Carro.id)).all()
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

def update_carro(db: Session, carro_id: int, carro: CarroUpdate):
    db_carro = get_carro(db, carro_id)
    db_carro.nome = carro.nome
    db_carro.ano_fabricacao = carro.ano_fabricacao
    db_carro.montadora_id = carro.montadora_id
    db.add(db_carro)
    db.commit()
    db.refresh(db_carro)
    return db_carro

def delete_carro(db: Session, carro_id: int):
    db_carro = get_carro(db, carro_id)
    db.delete(db_carro)
    db.commit()