from enum import Enum

class APIRoutes(str, Enum):
    USERS = "/api/v1/users"
    AUTHENTICATION = "/api/v1/authentication"
    FILES = "/api/v1/files"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"

    def __str__(self):
        return self.value
print(APIRoutes.AUTHENTICATION)