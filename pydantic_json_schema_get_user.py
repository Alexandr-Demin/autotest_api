from tools.assertions.schema import validate_json_schema
from client.private_http_builder import AuthenticationUserSchema
from client.users.private_users_client import get_private_users_client
from client.users.public_users_client import get_publick_users_client
from client.users.users_schema import GetUserResponseSchema
from pydantic_create_user import CreateUserRequestSchema
from tools.fakers import get_random_email



publick_user_client = get_publick_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password= "string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

create_user_response = publick_user_client.create_user(create_user_request)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_user_client = get_private_users_client(authentication_user)
get_user_response = private_user_client.get_user_api(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)