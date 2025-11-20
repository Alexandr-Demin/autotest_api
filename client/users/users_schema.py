from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserSchema(BaseModel):

    model_config=ConfigDict(populate_by_name=True)

    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str=Field(alias="lastName")
    first_name: str=Field(alias="firstName")
    middle_name: str=Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):

    model_config=ConfigDict(populate_by_name=True)

    """
    Структура тела создания пользователя
    """
    email: EmailStr
    password: str
    last_name: str=Field(alias="lastName")
    first_name: str=Field(alias="firstName")
    middle_name: str=Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):

    model_config=ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на обновление пользователя.
    """
    email: EmailStr | None
    last_name: str | None=Field(alias="lastName")
    first_name: str | None=Field(alias="firstName")
    middle_name: str | None=Field(alias="middleName")

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа бновления пользователя.
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа бновления пользователя.
    """
    user: UserSchema