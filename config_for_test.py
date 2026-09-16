from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

env_name = os.getenv("ENV", "local")

class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self)-> str:
        return str(self.url)

class TestDataConfig(BaseModel):
    __test__ = False
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f".env.{env_name}",
        env_file_encoding='utf-8',
        env_nested_delimiter="."
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig

settings = Settings()