from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateRequestData(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    код для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateRequestData) -> Response:
        """
        метод выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :param request: словарь с валидными параметрами
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
