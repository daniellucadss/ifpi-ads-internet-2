from sqlmodel import select, Session
from repository.models import Usuario, Montadora, Modelo, Veiculo
from schemas.user import UsuarioCreate, UsuarioLogin
from schemas.montadora import MontadoraCreate, MontadoraUpdate
from schemas.modelo import ModeloCreate, ModeloUpdate
from schemas.veiculo import VeiculoCreate, VeiculoUpdate

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario()
    db_usuario.username = usuario.username
    db_usuario.password = usuario.password
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)    
    return db_usuario

def get_usuario(db: Session, usuario: UsuarioLogin):
    usuario = db.exec(select(Usuario).where(Usuario.username == usuario.username, Usuario.password == usuario.password)).first()
    return usuario

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

def create_modelo(db: Session, modelo: ModeloCreate):
    db_modelo = Modelo()
    db_modelo.nome=modelo.nome, 
    db_modelo.montadora_id=modelo.montadora_id
    db_modelo.valor_referencia=modelo.valor_referencia
    db_modelo.ano_modelo=modelo.ano_modelo
    db_modelo.motorizacao=modelo.motorizacao
    db_modelo.turbo=modelo.turbo
    db_modelo.automatico=modelo.automatico
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)    
    return db_modelo

def get_modelos(db: Session):
    modelos = db.exec(select(Modelo).order_by(Modelo.id)).all()
    return modelos

def get_modelo(db: Session, modelo_id: int):
    modelo = db.exec(select(Modelo).where(Modelo.id == modelo_id)).first()
    if modelo:
        montadora = db.exec(select(Montadora).where(Montadora.id == modelo.montadora_id)).first()
        modelo.montadora = montadora 
    return modelo

def update_modelo(db: Session, modelo_id: int, modelo: ModeloUpdate):
    db_modelo = get_modelo(db, modelo_id)
    db_modelo.nome=modelo.nome, 
    db_modelo.montadora_id=modelo.montadora_id
    db_modelo.valor_referencia=modelo.valor_referencia
    db_modelo.ano_modelo=modelo.ano_modelo
    db_modelo.motorizacao=modelo.motorizacao
    db_modelo.turbo=modelo.turbo
    db_modelo.automatico=modelo.automatico
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

def delete_modelo(db: Session, modelo_id: int):
    db_modelo = get_modelo(db, modelo_id)
    db.delete(db_modelo)
    db.commit()

def create_veiculo(db: Session, veiculo: VeiculoCreate):
    db_veiculo = Veiculo()
    db_veiculo.modelo_id = veiculo.modelo_id
    db_veiculo.cor = veiculo.cor
    db_veiculo.ano_fabricacao = veiculo.ano_fabricacao
    db_veiculo.valor = veiculo.valor
    db_veiculo.placa = veiculo.placa
    db_veiculo.vendido = veiculo.vendido
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)    
    return db_veiculo

def get_veiculos(db: Session):
    veiculos = db.exec(select(Veiculo).order_by(Veiculo.id)).all()
    return veiculos

def get_veiculo(db: Session, veiculo_id: int):
    veiculo = db.exec(select(Veiculo).where(Veiculo.id == veiculo_id)).first()
    if veiculo:
        modelo = db.exec(select(Modelo).where(Modelo.id == veiculo.modelo_id)).first()
        veiculo.modelo = modelo 
    return veiculo

def get_veiculo(db: Session, veiculo_id: int):
    veiculo = db.exec(select(Veiculo).where(Veiculo.id == veiculo_id)).first()
    print(veiculo)
    if veiculo:
        modelo = db.exec(select(Modelo).where(Modelo.id == veiculo.modelo_id)).first()
        veiculo.modelo = modelo if modelo else None
    return veiculo

def update_veiculo(db: Session, veiculo_id: int, veiculo: VeiculoUpdate):
    db_veiculo = get_veiculo(db, veiculo_id)
    db_veiculo.modelo_id = veiculo.modelo_id
    db_veiculo.cor = veiculo.cor
    db_veiculo.ano_fabricacao = veiculo.ano_fabricacao
    db_veiculo.valor = veiculo.valor
    db_veiculo.placa = veiculo.placa
    db_veiculo.vendido = veiculo.vendido
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def delete_veiculo(db: Session, veiculo_id: int):
    db_veiculo = get_veiculo(db, veiculo_id)
    db.delete(db_veiculo)
    db.commit()