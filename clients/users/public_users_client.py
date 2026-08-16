from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа на создание пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    код для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        метод выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :param request: словарь с валидными параметрами
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.
    :return: Готовый к использованию объект httpx.Client.
    """
    return PublicUsersClient(client=get_public_http_client())
