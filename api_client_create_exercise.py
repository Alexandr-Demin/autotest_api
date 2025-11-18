from client.courses.courses_client import CreateBodyRequestDict, get_courses_client
from client.exercises.exercises_client import CreateExerciseRequestDict, get_exercises_client
from client.files.files_client import CreateFileRequestDict, get_files_client
from client.private_http_builder import AuthenticationUserDict
from client.users.public_users_client import CreateNewUser, get_publick_users_client
from tools.fakers import get_random_email


publick_user_client = get_publick_users_client()

create_user_request = CreateNewUser(
    email=get_random_email(),
    password="string1",
    lastName="string1",
    firstName="string1",
    middleName="string1"
)
create_user_response = publick_user_client.create_user(create_user_request)
print('Body', create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
file_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = file_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateBodyRequestDict(
     title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)


create_exercise_request = CreateExerciseRequestDict(
    title="Тестирование API",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=3,
    description="Базовый курс",
    estimatedTime="180"
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)