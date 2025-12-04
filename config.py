from pydantic_settings import BaseSettings
from pydantic import BaseModel, HttpUrl, FilePath, ConfigDict

class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        env_nested_delimiter = "."
    )
    http_client: HTTPClientConfig
    test_data: TestData

setting = Settings()