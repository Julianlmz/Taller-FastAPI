from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List
from Database import SessionDep
from Models import Lonchera, LoncheraCreate, LoncheraRead, LoncheraBase, Usuario

router = APIRouter(prefix="/loncheras", tags=["Loncheras"])


@router.post("/", response_model=LoncheraRead)
def create_lonchera(session: SessionDep, lonchera: LoncheraCreate):
    if not session.get(Usuario, lonchera.propietario_id):
        raise HTTPException(status_code=404, detail="Propietario no encontrado")

    db_lonchera = Lonchera.model_validate(lonchera)
    session.add(db_lonchera)
    session.commit()
    session.refresh(db_lonchera)
    return db_lonchera


@router.get("/", response_model=List[LoncheraRead])
def read_loncheras(session: SessionDep):
    loncheras = session.exec(select(Lonchera)).all()
    return loncheras


@router.get("/{lonchera_id}", response_model=LoncheraRead)
def read_lonchera(session: SessionDep, lonchera_id: int):
    lonchera = session.get(Lonchera, lonchera_id)
    if not lonchera:
        raise HTTPException(status_code=404, detail="Lonchera no encontrada")
    return lonchera


@router.patch("/{lonchera_id}", response_model=LoncheraRead)
def update_lonchera(session: SessionDep, lonchera_id: int, lonchera_update: LoncheraBase):
    db_lonchera = session.get(Lonchera, lonchera_id)
    if not db_lonchera:
        raise HTTPException(status_code=404, detail="Lonchera no encontrada")

    lonchera_data = lonchera_update.model_dump(exclude_unset=True)
    db_lonchera.sqlmodel_update(lonchera_data)

    session.add(db_lonchera)
    session.commit()
    session.refresh(db_lonchera)
    return db_lonchera


@router.delete("/{lonchera_id}")
def delete_lonchera(session: SessionDep, lonchera_id: int):
    lonchera = session.get(Lonchera, lonchera_id)
    if not lonchera:
        raise HTTPException(status_code=404, detail="Lonchera no encontrada")

    session.delete(lonchera)
    session.commit()
    return {"ok": True, "detail": "Lonchera eliminada"}
