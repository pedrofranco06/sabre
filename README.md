# SABRE — Sistema Automatizado de Busca e Resumo

Agente de IA que recebe um tema pelo Discord, pesquisa na Web e devolve um resumo estruturado em Markdown.
Case da subárea de IA do processo seletivo IEEE CEFET/RJ 2026.2.

## Como rodar

1. Instale o [uv](https://docs.astral.sh/uv/).
   - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Instale as dependências: `uv sync`
3. Copie `.env.example` para `.env` e preencha (veja abaixo).
4. Rode: `uv run python -m sabre`
5. No servidor SABRE-dev, use `/ola` e `/perguntar`.

## Seu bot de desenvolvimento

Cada integrante usa o **próprio** bot, para que todos possam rodar ao mesmo tempo sem conflito.

1. [Discord Developer Portal](https://discord.com/developers/applications) → New Application → `sabre-dev-<seu-nome>`.
2. Bot → Reset Token → copie para `DISCORD_TOKEN` no `.env`.
3. OAuth2 → URL Generator → scopes `bot` + `applications.commands`; permissões *Send Messages* e *Attach Files*. Abra a URL e adicione ao servidor SABRE-dev.
4. No Discord: Configurações → Avançado → Modo desenvolvedor. Clique com o botão direito no servidor → Copiar ID → `DISCORD_GUILD_ID`.
5. Chave do Groq em [console.groq.com](https://console.groq.com/keys) → `GROQ_API_KEY`. Confira em *Models* se o modelo de `LLM_MODEL` continua disponível.

## Fluxo de trabalho

- Cada tarefa é uma issue; branch `feat/<frente>-<descricao>`; PR com 1 aprovação de outra frente.
- Dependências sempre com `uv add` (nunca `pip install`).
- Nunca commitar o `.env`.
