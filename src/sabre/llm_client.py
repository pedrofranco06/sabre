from langchain.chat_models import init_chat_model

SYSTEM_PROMPT = (
    "Você é o SABRE, um assistente de pesquisa. "
    "Responda em português do Brasil, em no máximo 5 frases."
)


class LanguageModelClient:
    def __init__(self, model_name: str) -> None:
        self._chat_model = init_chat_model(model_name, temperature=0.2)

    async def ask(self, question: str) -> str:
        response = await self._chat_model.ainvoke([("system", SYSTEM_PROMPT), ("human", question)])
        return response.text
