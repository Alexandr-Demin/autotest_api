from client.errors_scheme import InternalErrorResponseSchema, ValidationErrorResponseScheme, ValidationErrorScheme
from client.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response, assert_validation_error_response
import allure
from config import setting

@allure.step("Check create file response")
def assert_create_file_response(
        request: CreateFileRequestSchema,
        response: CreateFileResponseSchema
):

    expected_url = f"{setting.http_client.client_url}static/{request.directory}/{request.filename}"
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")
    assert_equal(str(response.file.url), expected_url, "url")

@allure.step("Check file")
def assert_create_file(actual: FileSchema, expected: FileSchema):
    
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")

@allure.step("Check get file response")
def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    assert_create_file(get_file_response.file, create_file_response.file)

@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseScheme):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseScheme(
        detail=[
            ValidationErrorScheme(
                type="string_too_short",
                input="",
                location=["body", "filename"],
                message="String should have at least 1 character",
                context={"min_length": 1}
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file with empty directory response")    
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseScheme):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseScheme(
        detail=[
            ValidationErrorScheme(
                type="string_too_short",
                input="",
                location=["body", "directory"],
                message="String should have at least 1 character",
                context={"min_length": 1}
            )
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check file not found response")
def assert_get_file_incorrect_file_id_response(actual: ValidationErrorResponseScheme):
    expected = ValidationErrorResponseScheme(
        detail=[
            ValidationErrorScheme(
                type="uuid_parsing",
                input="incorrect-file-id",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"}
            )
        ]
    )
    assert_validation_error_response(actual, expected)
    