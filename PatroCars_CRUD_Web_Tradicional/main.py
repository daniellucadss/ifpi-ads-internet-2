from typing import Annotated
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, SQLModel
from crud import create_carro, delete_carro, get_carro, get_carros, create_montadora, get_montadora, get_montadoras, update_carro, update_montadora, delete_montadora
from schemas import CarroCreate, CarroUpdate, MontadoraCreate, MontadoraUpdate
from database import get_engine, get_session

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

SQLModel.metadata.create_all(get_engine())

SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/")
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

@app.get("/carros_lista")
async def carros_lista(request: Request, db: SessionDep):
    carros = get_carros(db)
    return templates.TemplateResponse("carros_lista.html", {"request": request, "carros": carros})

@app.get("/carro_adicionar")
async def carro_adicionar(request: Request, db: SessionDep):
    montadoras = get_montadoras(db)
    return templates.TemplateResponse("carro_adicionar.html", {"request": request, "montadoras": montadoras})

@app.post("/carro_adicionar")
async def carro_adicionar(db: SessionDep, carro: Annotated[CarroCreate, Form()]):
    create_carro(db, carro)
    return RedirectResponse("/carros_lista", status_code=303)

@app.get("/carro_detalhes/{carro_id}")
async def carro_detalhes(request: Request, db: SessionDep, carro_id: int):
    carro = get_carro(db, carro_id)
    return templates.TemplateResponse("carro_detalhes.html", {"request": request, "carro": carro})


@app.get("/carro_atualizar/{carro_id}")
async def carro_atualizar(request: Request, db: SessionDep, carro_id: int):
    montadoras = get_montadoras(db)
    carro = get_carro(db, carro_id)
    return templates.TemplateResponse("carro_atualizar.html", {"request": request, "carro": carro, "montadoras": montadoras})

@app.post("/carro_atualizar/{carro_id}")
async def carro_atualizar(db: SessionDep, carro_id: int, carro: Annotated[CarroUpdate, Form()]):
    update_carro(db, carro_id, carro)
    return RedirectResponse("/carros_lista", status_code=303)

@app.post("/carro_deletar/{carro_id}")
async def carro_deletar(db: SessionDep, carro_id: int):
    delete_carro(db, carro_id)
    return RedirectResponse("/carros_lista", status_code=303)