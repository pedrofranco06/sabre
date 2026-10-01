import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    discord_token: str
    discord_guild_id: int
    llm_model: str


def load_settings() -> Settings:
    load_dotenv()
    return Settings(
        discord_token=_require_env_variable("DISCORD_TOKEN"),
        discord_guild_id=int(_require_env_variable("DISCORD_GUILD_ID")),
        llm_model=_require_env_variable("LLM_MODEL"),
    )


def _require_env_variable(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"A variável {name} não está definida no arquivo .env")
    return value
