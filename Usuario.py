from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List
from Database import SessionDep
from Models import Usuario, UsuarioCreate, UsuarioRead, UsuarioBase

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioRead)
def create_user(session: SessionDep, user: UsuarioCreate):
    db_user = Usuario.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/", response_model=List[UsuarioRead])
def read_users(session: SessionDep):
    users = session.exec(select(Usuario)).all()
    return users


@router.get("/{user_id}", response_model=UsuarioRead)
def read_user(session: SessionDep, user_id: int):
    user = session.get(Usuario, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.patch("/{user_id}", response_model=UsuarioRead)
def update_user(session: SessionDep, user_id: int, user_update: UsuarioBase):
    db_user = session.get(Usuario, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user_data = user_update.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(user_data)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
def delete_user(session: SessionDep, user_id: int):
    user = session.get(Usuario, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    session.delete(user)
    session.commit()
    return {"ok": True, "detail": "Usuario eliminado"}