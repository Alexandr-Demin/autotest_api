from client.api_client import APIClient
from httpx import Response
from typing import TypedDict
from client.public_http_builder import get_public_http_client

class User (TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateNewUser(TypedDict):
    """
    Структура тела создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User




class PublicUsersClient(APIClient):


    def create_user_api(
            self, 
            request: CreateNewUser
            ) -> Response:
        """
        Метод выполняет создание пользователя

        :param request: Словарь с данными пользователя
        :return:  Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/users", json=request)
    
    def create_user(self, request: CreateNewUser) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()
    

def get_publick_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PublicUsersClient(client=get_public_http_client())