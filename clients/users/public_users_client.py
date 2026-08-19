from clients.api_client import APIClient
from httpx import Response
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema


class PublicUsersClient(APIClient):
    """
    код для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        метод выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :param request: словарь с валидными параметрами
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.
    :return: Готовый к использованию объект httpx.Client.
    """
    return PublicUsersClient(client=get_public_http_client())
