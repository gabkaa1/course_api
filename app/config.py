from pydantic_settings import BaseSettings
from pydantic import model_validator, ConfigDict



class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    model_config = ConfigDict(env_file=".env")
    DATABASE_URL: str = ""

    @model_validator(mode='after')
    def get_database_url(self) -> 'Settings':
        # ВАЖНО: теперь работаем с self, а не со словарем v
        self.DATABASE_URL = (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )
        # Можно добавить здесь любую другую логику валидации
        # if not self.DB_USER:
        #     raise ValueError('DB_USER не может быть пустым')
        
        # Всегда возвращать self для mode='after'
        return self
# Использование
# settings = Settings() # Здесь автоматически создастся DATABASE_URL
# print(settings.DATABASE_URL)
    

settings = Settings()

print(settings.DATABASE_URL)

