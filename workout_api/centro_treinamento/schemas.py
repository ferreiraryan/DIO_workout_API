from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do centro de treinamento", examples=["CT NL"], max_length=20)
    ]
    endereco: Annotated[
        str, Field(description="Endereco do centro de treinamento", examples=["Rua tal, numero tal"], max_length=60)
    ]
    proprietario: Annotated[
        str, Field(description="proprietario do centro de treinamento", examples=["Carlao"], max_length=30)
    ]
