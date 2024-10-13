from typing import Annotated
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, SQLModel
from crud import create_carro, get_carro, get_carros, create_montadora, get_montadora, get_montadoras
from schemas import CarroCreate, MontadoraCreate
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

@app.get("/montadora_formulario")
async def montadora_formulario(request: Request):
    return templates.TemplateResponse("montadora_formulario.html", {"request": request})

@app.post("/montadora_formulario")
async def montadora_formulario(db: SessionDep, montadora: Annotated[MontadoraCreate, Form()]):
    create_montadora(db, montadora)
    return RedirectResponse("/montadoras_lista", status_code=303)

@app.get("/montadora/{montadora_id}")
async def montadora_detalhes(request: Request, montadora_id: int, db: SessionDep):
    montadora = get_montadora(db, montadora_id)
    return templates.TemplateResponse("montadora_detalhes.html", {"request": request, "montadora": montadora})

@app.get("/carros_lista")
async def carros_lista(request: Request, db: SessionDep):
    carros = get_carros(db)
    return templates.TemplateResponse("carros_lista.html", {"request": request, "carros": carros})

@app.get("/carro_formulario")
async def carro_formulario(request: Request, db: SessionDep):
    montadoras = get_montadoras(db)
    return templates.TemplateResponse("carro_formulario.html", {"request": request, "montadoras": montadoras})

@app.post("/carro_formulario")
async def carro_formulario(db: SessionDep, carro: Annotated[CarroCreate, Form()]):
    create_carro(db, carro)
    return RedirectResponse("/carros_lista", status_code=303)

@app.get("/carro/{carro_id}")
async def carro_detalhes(request: Request, carro_id: int, db: SessionDep):
    carro = get_carro(db, carro_id)
    return templates.TemplateResponse("carro_detalhes.html", {"request": request, "carro": carro})


