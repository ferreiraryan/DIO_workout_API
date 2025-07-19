from inspect import Traceback
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from starlette.status import HTTP_404_NOT_FOUND

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import (
    CentroTreinamentoIn,
    CentroTreinamentoOut,
)
from workout_api.contrib.dependencies import DataBaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar um novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DataBaseDependency,
    centro_treinamento_in: CentroTreinamentoIn = Body(...),
) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(
        id=uuid4(), **centro_treinamento_in.model_dump()
    )
    centro_treinamento_model = CentroTreinamentoModel(
        **centro_treinamento_out.model_dump()
    )

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out


@router.get(
    "/",
    summary="Consultar todas os centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DataBaseDependency) -> list[CentroTreinamentoOut]:
    centros_treinamento: list[CentroTreinamentoOut] = (
        (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()  # type: ignore
    )

    return centros_treinamento


@router.get(
    "/{id}",
    summary="Consultar um centro de treinamento pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: DataBaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_db: Optional[CentroTreinamentoModel] = (
        (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not centro_treinamento_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"centro_treinamento não encontrada no id: {id}",
        )

    return CentroTreinamentoOut.model_validate(centro_treinamento_db)
