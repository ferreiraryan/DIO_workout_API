from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from fastapi_pagination import Page

from fastapi_pagination.ext.sqlalchemy import paginate
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaResumido, AtletaUpdate
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.dependencies import DataBaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar um novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(
    db_session: DataBaseDependency, atleta_in: AtletaIn = Body(...)
) -> AtletaOut:
    categoria = (
        (
            await db_session.execute(
                select(CategoriaModel).filter_by(nome=atleta_in.categoria.nome)
            )
        )
        .scalars()
        .first()
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Categoria {atleta_in.categoria.nome} nao encontrada",
        )

    centro_treinamento = (
        (
            await db_session.execute(
                select(CentroTreinamentoModel).filter_by(
                    nome=atleta_in.centro_treinamento.nome
                )
            )
        )
        .scalars()
        .first()
    )

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Centro de treinamento {atleta_in.centro_treinamento.nome} nao encontrado",
        )
    try:
        atleta_out = AtletaOut(
            id=uuid4(),
            created_at=datetime.now(timezone.utc).replace(tzinfo=None),
            **atleta_in.model_dump(),
        )
        atleta_model = AtletaModel(
            **atleta_out.model_dump(exclude={"categoria", "centro_treinamento"})
        )

        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro ao inserir os dados n banco",
        )
    return atleta_out


@router.get(
    "/",
    summary="Consultar todos os Atletas",
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaOut],
)
async def query(db_session: DataBaseDependency) -> Page[AtletaOut]:
    query = select(AtletaModel).options(
        selectinload(AtletaModel.categoria),
        selectinload(AtletaModel.centro_treinamento),
    )

    return await paginate(db_session, query)


# @router.get(
#     "/",
#     summary="Consultar todos os atletas",
#     status_code=status.HTTP_200_OK,
#     response_model=list[AtletaOut],
# )
# async def query(db_session: DataBaseDependency) -> list[AtletaOut]:
#     atletas: list[AtletaOut] = (
#         (await db_session.execute(select(AtletaModel))).scalars().all()  # type: ignore
#     )
#     return [AtletaOut.model_validate(atleta) for atleta in atletas]


@router.get(
    "/{id}",
    summary="Consultar um atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(id: UUID4, db_session: DataBaseDependency) -> AtletaOut:
    query = select(AtletaModel).options(
        selectinload(AtletaModel.categoria),
        selectinload(AtletaModel.centro_treinamento),
    )

    # ... seus filtros ...

    # Esta chamada agora vai usar a função paginate correta
    # por causa do import explícito.
    return await paginate(db_session, query)


@router.post(
    "/{id}",
    summary="Editar um atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(
    id: UUID4, db_session: DataBaseDependency, atleta_up: AtletaUpdate = Body(...)
) -> AtletaOut:
    atleta_db: Optional[AtletaModel] = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrada no id: {id}",
        )
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta_db, key, value)

    await db_session.commit()
    await db_session.refresh(atleta_db)
    return atleta_db


@router.delete(
    "/{id}", summary="Deletar um atleta pelo id", status_code=status.HTTP_204_NO_CONTENT
)
async def query(id: UUID4, db_session: DataBaseDependency) -> None:
    atleta_db: Optional[AtletaModel] = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not atleta_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrada no id: {id}",
        )

    await db_session.delete(atleta_db)
    await db_session.commit()
