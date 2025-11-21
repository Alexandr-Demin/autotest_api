from client.courses.courses_client import get_courses_client
from client.courses.courses_schema import CreateBodyRequestSchema
from client.exercises.exercises_client import get_exercises_client
from client.exercises.exercises_schema import CreateExerciseRequestSchema
from client.files.files_client import get_files_client
from client.private_http_builder import AuthenticationUserSchema
from client.users.public_users_client import get_publick_users_client
from tools.fakers import fake
from client.users.users_schema import CreateUserRequestSchema
from client.files.files_schema import CreateFileRequestSchema


publick_user_client = get_publick_users_client()

create_user_request = CreateUserRequestSchema()
create_user_response = publick_user_client.create_user(create_user_request)
print('Body', create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
file_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
create_file_response = file_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateBodyRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)


create_exercise_request = CreateExerciseRequestSchema()
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)