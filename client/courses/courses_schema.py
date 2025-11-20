from pydantic import BaseModel, Field, ConfigDict
from client.users.users_schema import UserSchema
from client.files.files_schema import FileSchema


class CourseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    description: str
    preview_file: FileSchema=Field(alias="previewFile")
    estimated_time: str=Field(alias="estimatedTime")
    created_by_user: UserSchema=Field(alias="createdByUser")

class GetRequestQuerySchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на получение списка курсов.
    """
    
    user_id: str=Field(alias="useId")

class CreateBodyRequestSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на создание курса.
    """

    title: str
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    description: str
    estimated_time: str=Field(alias="estimatedTime")
    preview_file_id: str=Field(alias="previewFileId")
    created_by_user_id: str=Field(alias="createdByUserId")

class CourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class UpdateBodyRequestSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на обновление курса.
    """

    title: str | None
    max_score: int | None=Field(alias="maxScore")
    min_score: int | None=Field(alias="minScore")
    description: str | None
    estimated_time: str | None=Field(alias="estimatedTime")