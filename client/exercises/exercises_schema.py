from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры задания.
    """
    id: str
    title: str
    course_id: str=Field(alias="courseId")
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    order_index: int=Field(alias="orderIndex")
    description: str
    estimated_time: str=Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение задания..
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на получение списка заданий.
    """
    user_id: str=Field(alias="useId")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    course_id: str=Field(alias="courseId")
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    order_index: int=Field(alias="orderIndex")
    description: str
    estimated_time: str=Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    max_score: int | None=Field(alias="maxScore")
    min_score: int | None=Field(alias="minScore")
    order_index: int | None=Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None=Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    order_index: int=Field(alias="orderIndex")
    description: str
    estimated_time: str=Field(alias="estimatedTime")