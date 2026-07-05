from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name :str
    app_version: str
    app_env: str

    ai_provider: str
    ai_api_key: str

    github_token: str

    supabase_url: str
    supabase_anon_key: str

    frontend_url: str

    class Config:
        env_file = ".env"

settings = Settings()
