from tools.assertions.schema import validate_json_schema
from client.users.public_users_client import get_publick_users_client
from client.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response
import pytest

@pytest.mark.users 
@pytest.mark.regression
def test_crate_user():
    
    publick_user_client = get_publick_users_client()
    request = CreateUserRequestSchema()
    response = publick_user_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())
