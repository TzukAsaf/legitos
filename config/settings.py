from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NUTRITIONIX_API_URL: str
    NUTRITIONIX_APP_ID: str
    NUTRITIONIX_APP_KEY: SecretStr


settings = Settings()
