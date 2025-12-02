from http import HTTPStatus
from client.authentication.authentication_client import AuthenticationClient
from client.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest
import allure
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.LMS)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Test login")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.LOGIN) 
    def test_login(self,function_user: UserFixture, authentication_client: AuthenticationClient):

        request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
        

    


    


    