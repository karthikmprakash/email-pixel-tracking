from pydantic import BaseSettings


class Settings(BaseSettings):
    smtp_email: str
    smtp_server: str
    smtp_password: str
    receiver_email: str
    server_url: str = "http://localhost:8000"

    class Config:
        env_file = ".env"


settings = Settings()
