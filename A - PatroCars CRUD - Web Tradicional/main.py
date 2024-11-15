from typing import Annotated
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, SQLModel
from repository.operations import create_montadora, create_usuario, create_veiculo, delete_veiculo, get_montadora, get_montadoras, get_usuario, get_veiculo, get_veiculos, update_montadora, delete_montadora, create_modelo, get_modelo, get_modelos, update_modelo, delete_modelo, update_veiculo
from schemas.montadora import MontadoraCreate, MontadoraUpdate
from schemas.modelo import ModeloCreate, ModeloUpdate
from schemas.user import UsuarioCreate, UsuarioLogin
from schemas.veiculo import VeiculoCreate, VeiculoUpdate
from repository.connection import get_engine, get_session

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

SQLModel.metadata.create_all(get_engine())

SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/cadastro")
async def post_cadastro(request: Request, db: SessionDep, usuario_data: Annotated[UsuarioCreate, Form()]):
    usuario = get_usuario(db, usuario_data)

    if usuario:
        return templates.TemplateResponse("cadastro.html", {"request": request, "error": "Usuário já cadastrado"})

    create_usuario(db, usuario_data)
    return RedirectResponse(url="/login", status_code=303)

@app.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def post_login(request: Request, db: SessionDep, usuario_data: Annotated[UsuarioLogin, Form()]):
    usuario = get_usuario(db, usuario_data)
    if not usuario:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Nome de usuário ou senha incorretos"})
    return templates.TemplateResponse("index.html", {"request": request, "message": f"Bem-vindo, {usuario.username}!"})

@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/montadoras_lista")
async def montadoras_lista(request: Request, db: SessionDep):
    montadoras = get_montadoras(db)
    return templates.TemplateResponse("montadoras_lista.html", {"request": request, "montadoras": montadoras})

@app.get("/montadora_adicionar")
async def montadora_adicionar(request: Request):
    return templates.TemplateResponse("montadora_adicionar.html", {"request": request})

@app.post("/montadora_adicionar")
async def montadora_adicionar(db: SessionDep, montadora: Annotated[MontadoraCreate, Form()]):
    create_montadora(db, montadora)
    return RedirectResponse("/montadoras_lista", status_code=303)

@app.get("/montadora_detalhes/{montadora_id}")
async def montadora_detalhes(request: Request, db: SessionDep, montadora_id: int):
    montadora = get_montadora(db, montadora_id)
    return templates.TemplateResponse("montadora_detalhes.html", {"request": request, "montadora": montadora})

@app.get("/montadora_atualizar/{montadora_id}")
async def montadora_atualizar(request: Request, db: SessionDep, montadora_id: int):
    montadora = get_montadora(db, montadora_id)
    return templates.TemplateResponse("montadora_atualizar.html", {"request": request, "montadora": montadora})

@app.post("/montadora_atualizar/{montadora_id}")
async def montadora_atualizar(db: SessionDep, montadora_id: int, montadora: Annotated[MontadoraUpdate, Form()]):
    update_montadora(db, montadora_id, montadora)
    return RedirectResponse("/montadoras_lista", status_code=303)

@app.post("/montadora_deletar/{montadora_id}")
async def montadora_deletar(db: SessionDep, montadora_id: int):
    delete_montadora(db, montadora_id)
    return RedirectResponse("/montadoras_lista", status_code=303)

@app.get("/modelos_lista")
async def modelos_lista(request: Request, db: SessionDep):
    modelos = get_modelos(db)
    return templates.TemplateResponse("modelos_lista.html", {"request": request, "modelos": modelos})

@app.get("/modelo_adicionar")
async def modelo_adicionar(request: Request, db: SessionDep):
    montadoras = get_montadoras(db)
    return templates.TemplateResponse("modelo_adicionar.html", {"request": request, "montadoras": montadoras})

@app.post("/modelo_adicionar")
async def modelo_adicionar(db: SessionDep, modelo: Annotated[ModeloCreate, Form()]):
    create_modelo(db, modelo)
    return RedirectResponse("/modelos_lista", status_code=303)

@app.get("/modelo_detalhes/{modelo_id}")
async def modelo_detalhes(request: Request, db: SessionDep, modelo_id: int):
    modelo = get_modelo(db, modelo_id)
    return templates.TemplateResponse("modelo_detalhes.html", {"request": request, "modelo": modelo})

@app.get("/modelo_atualizar/{modelo_id}")
async def modelo_atualizar(request: Request, db: SessionDep, modelo_id: int):
    montadoras = get_montadoras(db)
    modelo = get_modelo(db, modelo_id)
    return templates.TemplateResponse("modelo_atualizar.html", {"request": request, "modelo": modelo, "montadoras": montadoras})

@app.post("/modelo_atualizar/{modelo_id}")
async def modelo_atualizar(db: SessionDep, modelo_id: int, modelo: Annotated[ModeloUpdate, Form()]):
    update_modelo(db, modelo_id, modelo)
    return RedirectResponse("/modelos_lista", status_code=303)

@app.post("/modelo_deletar/{modelo_id}")
async def modelo_deletar(db: SessionDep, modelo_id: int):
    delete_modelo(db, modelo_id)
    return RedirectResponse("/modelos_lista", status_code=303)

@app.get("/veiculos_lista")
async def veiculos_lista(request: Request, db: SessionDep):
    veiculos = get_veiculos(db)
    return templates.TemplateResponse("veiculos_lista.html", {"request": request, "veiculos": veiculos})

@app.get("/veiculo_adicionar")
async def veiculo_adicionar(request: Request, db: SessionDep):
    modelos = get_modelos(db)
    return templates.TemplateResponse("veiculo_adicionar.html", {"request": request, "modelos": modelos})

@app.post("/veiculo_adicionar")
async def veiculo_adicionar(db: SessionDep, veiculo: Annotated[VeiculoCreate, Form()]):
    create_veiculo(db, veiculo)
    return RedirectResponse("/veiculos_lista", status_code=303)

@app.get("/veiculo_detalhes/{veiculo_id}")
async def veiculo_detalhes(request: Request, db: SessionDep, veiculo_id: int):
    veiculo = get_veiculo(db, veiculo_id)
    return templates.TemplateResponse("veiculo_detalhes.html", {"request": request, "veiculo": veiculo})

@app.get("/veiculo_atualizar/{veiculo_id}")
async def veiculo_atualizar(request: Request, db: SessionDep, veiculo_id: int):
    modelos = get_modelos(db)
    veiculo = get_veiculo(db, veiculo_id)
    return templates.TemplateResponse("veiculo_atualizar.html", {"request": request, "veiculo": veiculo, "modelos": modelos})

@app.post("/veiculo_atualizar/{veiculo_id}")
async def veiculo_atualizar(db: SessionDep, veiculo_id: int, veiculo: Annotated[VeiculoUpdate, Form()]):
    update_veiculo(db, veiculo_id, veiculo)
    return RedirectResponse("/veiculos_lista", status_code=303)

@app.post("/veiculo_deletar/{veiculo_id}")
async def veiculo_deletar(db: SessionDep, veiculo_id: int):
    delete_veiculo(db, veiculo_id)
    return RedirectResponse("/veiculos_lista", status_code=303)