from client.api_client import APIClient
from httpx import Response
from typing import TypedDict


class CreateNewUser(TypedDict):
    """
    Структура тела создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str



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