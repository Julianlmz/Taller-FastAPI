from fastapi import FastAPI
from Database import engine
from sqlmodel import SQLModel
import Alimentos
import Loncheras
import Pedidos
import Usuario

app = FastAPI(
    title="API de Nutribox",
    description="API para gestionar usuarios, loncheras, alimentos y pedidos."
)

SQLModel.metadata.create_all(engine)

app.include_router(Usuario.router)
app.include_router(Loncheras.router)
app.include_router(Alimentos.router)
app.include_router(Pedidos.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"mensaje": "Bienvenido a la API de Nutribox"}