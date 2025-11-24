from client.users.private_users_client import PrivateUsersClient
from tests.conftest import UserFixture
from tools.assertions.schema import validate_json_schema
from client.users.public_users_client import PublicUsersClient
from client.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import pytest

@pytest.mark.users 
@pytest.mark.regression
def test_crate_user(publick_user_client: PublicUsersClient):
    
    request = CreateUserRequestSchema()
    response = publick_user_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())

@pytest.mark.users 
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)

    validate_json_schema(response.json(), response_data.model_json_schema())