from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List
from Database import SessionDep
from Models import Alimento, AlimentoCreate, AlimentoRead, AlimentoBase

router = APIRouter(prefix="/alimentos", tags=["Alimentos"])


@router.post("/", response_model=AlimentoRead)
def create_alimento(session: SessionDep, alimento: AlimentoCreate):
    db_alimento = Alimento.model_validate(alimento)
    session.add(db_alimento)
    session.commit()
    session.refresh(db_alimento)
    return db_alimento


@router.get("/", response_model=List[AlimentoRead])
def read_alimentos(session: SessionDep):
    alimentos = session.exec(select(Alimento)).all()
    return alimentos


@router.get("/{alimento_id}", response_model=AlimentoRead)
def read_alimento(session: SessionDep, alimento_id: int):
    alimento = session.get(Alimento, alimento_id)
    if not alimento:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")
    return alimento


@router.patch("/{alimento_id}", response_model=AlimentoRead)
def update_alimento(session: SessionDep, alimento_id: int, alimento_update: AlimentoBase):
    db_alimento = session.get(Alimento, alimento_id)
    if not db_alimento:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")

    alimento_data = alimento_update.model_dump(exclude_unset=True)
    db_alimento.sqlmodel_update(alimento_data)

    session.add(db_alimento)
    session.commit()
    session.refresh(db_alimento)
    return db_alimento


@router.delete("/{alimento_id}")
def delete_alimento(session: SessionDep, alimento_id: int):
    alimento = session.get(Alimento, alimento_id)
    if not alimento:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")

    session.delete(alimento)
    session.commit()
    return {"ok": True, "detail": "Alimento eliminado"}
