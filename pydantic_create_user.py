from pydantic import BaseModel, ConfigDict, EmailStr,Field



class UserSchema(BaseModel):
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
    Описание структуры запроса на создание пользователя.
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