from client.api_client import APIClient
from httpx import Response
from typing import TypedDict
from client.public_http_builder import get_public_http_client
from client.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import allure
from tools.routes import APIRoutes
from client.api_coverage import tracker


class PublicUsersClient(APIClient):

    @allure.step("Create user")
    @tracker.track_coverage_httpx(APIRoutes.USERS)
    def create_user_api(
            self, 
            request: CreateUserRequestSchema
            ) -> Response:
        """
        Метод выполняет создание пользователя

        :param request: Словарь с данными пользователя
        :return:  Ответ от сервера в виде объекта httpx.Response
        """

        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))
    
    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)
    

def get_publick_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PublicUsersClient(client=get_public_http_client())