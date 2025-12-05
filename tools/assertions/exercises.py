

from client.errors_scheme import InternalErrorResponseSchema
from client.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, ExerciseSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal, assert_lenght
from tools.assertions.errors import assert_internal_error_response
import allure
from tools.logger import get_logger

logger = get_logger("EXECISES_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseRequestSchema, expected: CreateExerciseResponseSchema):
    logger.info("Check create exercise response")
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(expected.exercise.title, actual.title, "title")
    assert_equal(expected.exercise.max_score, actual.max_score, "max_score")
    assert_equal(expected.exercise.min_score, actual.min_score, "min_score")
    assert_equal(expected.exercise.order_index, actual.order_index, "order_index")
    assert_equal(expected.exercise.description, actual.description, "description")
    assert_equal(expected.exercise.estimated_time, actual.estimated_time, "estimated_time")
    assert_equal(expected.exercise.course_id, actual.course_id, "course_id")

@allure.step("Check exercise")
def assert_exercises(actual: ExerciseSchema, expected: ExerciseSchema):
    logger.info("Check exercise")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.course_id, expected.course_id, "course_id")

@allure.step("Check get exercise response")    
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
   logger.info("Check get exercise response")
   """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные задания не совпадают.
    """ 
   assert_exercises(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    logger.info("Check update exercise response")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercise_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    logger.info("Check get exercises response")
    assert_lenght(get_exercise_response.exercises, create_exercise_responses, "courses")
    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercises(get_exercise_response.exercises[index], create_exercise_response.exercise)