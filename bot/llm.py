import logging

from openai import AsyncOpenAI

from bot.config import get_settings

logger = logging.getLogger(__name__)


def _build_messages(system_prompt: str, history: list[dict], message: str) -> list[dict]:
    return [{"role": "system", "content": system_prompt}, *history, {"role": "user", "content": message}]


async def ask_llm(history: list[dict], message: str) -> str:
    s = get_settings()
    client = AsyncOpenAI(api_key=s["LLM_API_KEY"], base_url=s["LLM_BASE_URL"])

    try:
        resp = await client.chat.completions.create(
            model=s["MODEL_NAME"],
            messages=_build_messages(s["SYSTEM_PROMPT"], history, message),
        )
    except Exception as e:
        logger.exception("LLM request failed: %s", e)
        raise

    content = resp.choices[0].message.content
    return (content or "").strip()
