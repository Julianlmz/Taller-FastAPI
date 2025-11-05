from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List
from Database import SessionDep
from Models import Pedido, PedidoCreate, PedidoRead, PedidoBase, Usuario, Alimento

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("/", response_model=PedidoRead)
def create_pedido(session: SessionDep, pedido: PedidoCreate):
    if not session.get(Usuario, pedido.cliente_id):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    pedido_data = pedido.model_dump(exclude={"alimentos_ids"})
    db_pedido = Pedido(**pedido_data)
    for alimento_id in pedido.alimentos_ids:
        alimento = session.get(Alimento, alimento_id)
        if not alimento:
            raise HTTPException(status_code=404, detail=f"Alimento id {alimento_id} no encontrado")
        db_pedido.alimentos.append(alimento)
    session.add(db_pedido)
    session.commit()
    session.refresh(db_pedido)
    return db_pedido


@router.get("/", response_model=List[PedidoRead])
def read_pedidos(session: SessionDep):
    pedidos = session.exec(select(Pedido)).all()
    return pedidos


@router.get("/{pedido_id}", response_model=PedidoRead)
def read_pedido(session: SessionDep, pedido_id: int):
    pedido = session.get(Pedido, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.patch("/{pedido_id}", response_model=PedidoRead)
def update_pedido(session: SessionDep, pedido_id: int, pedido_update: PedidoBase):
    db_pedido = session.get(Pedido, pedido_id)
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    pedido_data = pedido_update.model_dump(exclude_unset=True)
    db_pedido.sqlmodel_update(pedido_data)

    session.add(db_pedido)
    session.commit()
    session.refresh(db_pedido)
    return db_pedido


@router.delete("/{pedido_id}")
def delete_pedido(session: SessionDep, pedido_id: int):
    pedido = session.get(Pedido, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    session.delete(pedido)
    session.commit()
    return {"ok": True, "detail": "Pedido eliminado"}
