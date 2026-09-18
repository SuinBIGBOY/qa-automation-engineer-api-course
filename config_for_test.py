from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from typing import Self


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
    allure_results_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)
        return Settings(allure_results_dir=allure_results_dir)

settings = Settings.initialize()
