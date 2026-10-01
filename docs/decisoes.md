# Decisões técnicas

Registro das escolhas da equipe e do motivo de cada uma (alimenta a Metodologia do relatório).

| Data | Decisão | Escolha | Por quê |
|---|---|---|---|
| 01/10/2026 | LLM | Groq (modelo definido em `LLM_MODEL` no `.env`) | Rápido e gratuito; trocar para Gemini muda só o `.env`. Confirmar com o teste comparativo T5 |
| 01/10/2026 | Framework de agente | LangChain v1 | O PDF de recomendação indica LangChain/LlamaIndex como mais adequados para bot de Discord que o Google ADK |
| 01/10/2026 | Busca web | Tavily, com `ddgs` de reserva | Devolve conteúdo limpo; o `ddgs` não pede chave mas sofre bloqueio por taxa |
| 01/10/2026 | Python | 3.12 | Evita o erro de `audioop` removido no 3.13 |
| 01/10/2026 | Dependências | uv | Recomendado no PDF; `uv run` dispensa ativar ambiente virtual |
