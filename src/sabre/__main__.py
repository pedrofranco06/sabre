import logging

from sabre.config import load_settings
from sabre.discord_bot import SabreBot
from sabre.llm_client import LanguageModelClient


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
    )
    settings = load_settings()
    llm_client = LanguageModelClient(settings.llm_model)
    bot = SabreBot(settings, llm_client)
    bot.run(settings.discord_token, log_handler=None)


if __name__ == "__main__":
    main()
