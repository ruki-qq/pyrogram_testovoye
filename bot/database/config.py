from pydantic_settings import BaseSettings, SettingsConfigDict


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="db_")

    user: str
    password: str
    host: str
    port: int
    name: str

    @property
    def url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        )

    echo: bool = True


db_config = DBConfig()
