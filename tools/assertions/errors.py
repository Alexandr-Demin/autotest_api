from client.errors_scheme import InternalErrorResponseSchema, ValidationErrorResponseScheme, ValidationErrorScheme
from tools.assertions.base import assert_equal, assert_lenght
import allure
from tools.logger import get_logger

logger = get_logger("ERRORS_ASEERTIONS")

@allure.step("Check validation error")
def assert_validate_errors(
        actual: ValidationErrorScheme, 
        expected: ValidationErrorScheme
):
    logger.info("Check validation error")
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """

    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.location, expected.location, "location")
    assert_equal(actual.message, expected.message, "type")
    assert_equal(actual.context, expected.context, "type")

@allure.step("Check validation error response")
def assert_validation_error_response(
        actual: ValidationErrorResponseScheme,
        expected: ValidationErrorResponseScheme
):
    logger.info("Check validation error response")
    """
    Проверяет, что объект ответа API с ошибками валидации (`ValidationErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_lenght(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validate_errors(actual.details[index], detail)

@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema, 
        expected: InternalErrorResponseSchema
):
    logger.info("Check internal error response")
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.details, expected.details, "details")