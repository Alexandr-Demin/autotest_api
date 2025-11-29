from typing import Any
from pydantic import BaseModel, Field, ConfigDict

class ValidationErrorScheme(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    location: list[str]=Field(alias="loc")
    message: str=Field(alias="msg")
    context: dict[str, Any]=Field(alias="ctx")

class ValidationErrorResponseScheme(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorScheme]=Field(alias="detail")

class InternalErrorResponseSchema(BaseModel):
    """
    Модель для описания внутренней ошибки.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str=Field(alias="detail")