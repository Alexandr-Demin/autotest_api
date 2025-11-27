import pytest
from pydantic import BaseModel
from client.courses.courses_client import CoursesClient, get_courses_client
from client.courses.courses_schema import CreateBodyRequestSchema, CourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture

class CorseFixture(BaseModel):
    request: CreateBodyRequestSchema
    response: CourseResponseSchema


@pytest.fixture
def course_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
    course_client: CoursesClient, 
    function_file: FileFixture, 
    function_user: UserFixture
    ) -> CorseFixture:
    request = CreateBodyRequestSchema(
        preview_file_id = function_file.response.file.id,
        created_by_user_id = function_user.response.user.id)
    response = course_client.create_course(request)
    return CorseFixture(request=request, response=response)