import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("database_url")

def get_engine():
  engine = create_engine(database_url)
  return engine

def get_session():
    with Session(get_engine()) as session:
        yield session