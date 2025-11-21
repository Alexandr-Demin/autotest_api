from assertions.schema import validate_json_schema
from client.users.public_users_client import get_publick_users_client
from client.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import get_random_email 


publick_user_client = get_publick_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = publick_user_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)
