from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
import datetime

class UsuarioBase(SQLModel):
    email: str = Field(unique=True, index=True)
    nombre: str


class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str
    loncheras: List["Lonchera"] = Relationship(back_populates="propietario")
    pedidos: List["Pedido"] = Relationship(back_populates="cliente")


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioRead(UsuarioBase):
    id: int


class LoncheraBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None


class Lonchera(LoncheraBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    propietario_id: int = Field(foreign_key="usuario.id")
    propietario: Usuario = Relationship(back_populates="loncheras")


class LoncheraCreate(LoncheraBase):
    propietario_id: int


class LoncheraRead(LoncheraBase):
    id: int
    propietario_id: int


class AlimentoBase(SQLModel):
    nombre: str = Field(index=True)
    calorias: float
    descripcion: Optional[str] = None


class Alimento(AlimentoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class AlimentoCreate(AlimentoBase):
    pass


class AlimentoRead(AlimentoBase):
    id: int


class PedidoBase(SQLModel):
    fecha: datetime.date
    estado: str = Field(default="pendiente")


class Pedido(PedidoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="usuario.id")
    cliente: Usuario = Relationship(back_populates="pedidos")


class PedidoCreate(PedidoBase):
    cliente_id: int


class PedidoRead(PedidoBase):
    id: int
    cliente_id: int
