import logging

import discord
from discord import app_commands

from sabre.config import Settings
from sabre.llm_client import LanguageModelClient

DISCORD_MESSAGE_LIMIT = 2000
logger = logging.getLogger(__name__)


class SabreBot(discord.Client):
    def __init__(self, settings: Settings, llm_client: LanguageModelClient) -> None:
        super().__init__(intents=discord.Intents.default())
        self.command_tree = app_commands.CommandTree(self)
        self._test_guild = discord.Object(id=settings.discord_guild_id)
        self._llm_client = llm_client
        self._register_commands()

    async def setup_hook(self) -> None:
        # Sincronizar no servidor de teste faz o comando aparecer na hora
        self.command_tree.copy_global_to(guild=self._test_guild)
        await self.command_tree.sync(guild=self._test_guild)

    async def on_ready(self) -> None:
        logger.info("Bot conectado como %s", self.user)

    def _register_commands(self) -> None:
        @self.command_tree.command(name="ola", description="Verifica se o SABRE está online")
        async def say_hello(interaction: discord.Interaction) -> None:
            await interaction.response.send_message("Olá! O SABRE está online.")

        @self.command_tree.command(
            name="perguntar", description="Faz uma pergunta ao modelo de linguagem"
        )
        @app_commands.describe(pergunta="O que você quer saber")
        async def ask_language_model(interaction: discord.Interaction, pergunta: str) -> None:
            await interaction.response.defer(thinking=True)  # o Discord exige resposta em 3 s
            try:
                answer = await self._llm_client.ask(pergunta)
            except Exception:
                logger.exception("Falha ao consultar o LLM")
                await interaction.followup.send(
                    "Não consegui falar com o modelo agora. Tente de novo em 1 minuto."
                )
                return
            await interaction.followup.send(_fit_discord_limit(answer))


def _fit_discord_limit(text: str) -> str:
    if len(text) <= DISCORD_MESSAGE_LIMIT:
        return text
    return text[: DISCORD_MESSAGE_LIMIT - 3] + "..."
