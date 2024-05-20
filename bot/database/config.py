import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_prefix="postgres_"
    )

    user: str
    password: str
    host: str
    port: int
    db: str

    @property
    def url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        )

    echo: bool = False


db_config = DBConfig()
