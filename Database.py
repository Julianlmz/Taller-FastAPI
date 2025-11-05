from typing import Annotated
from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends, FastAPI


db_name = "pets.sqlite3"
db_url = f"sqlite:///{db_name}"

engine = create_engine(db_url)

def create_tables(app:FastAPI):
    SQLModel.metadata.create_all(bind=engine)
    yield

def get_session() -> Session:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]



