from http import HTTPStatus
import pytest
import allure
from allure_commons.types import Severity

from client.courses.courses_client import CoursesClient
from client.courses.courses_schema import CourseResponseSchema, CreateBodyRequestSchema, GetCoursesResponseSchema, GetRequestQuerySchema, UpdateBodyRequestSchema, UpdateCourseResponseSchema
from fixtures.courses import CorseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.course import assert_create_course_response, assert_get_courses_response, assert_update_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
class TestCorses:
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get courses")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.GET_ENTITIES) 
    def test_get_courses(self, course_client: CoursesClient, function_course: CorseFixture, function_user: UserFixture):
        query = GetRequestQuerySchema(user_id=function_user.response.user.id)
        response = course_client.get_api_courses(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update courses")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY) 
    def test_update_course(self, course_client: CoursesClient, function_course: CorseFixture):
        request = UpdateBodyRequestSchema()
        response = course_client.update_course_api(request, function_course.response.course.id)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create courses")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY) 
    def test_create_course(
            self,
            function_file: FileFixture,
            function_user: UserFixture,
            course_client: CoursesClient
        ):

        request = CreateBodyRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )
        response = course_client.create_course_api(request)
        response_data = CourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())