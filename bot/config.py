import os

from dotenv import load_dotenv

load_dotenv()


def get_settings() -> dict[str, str]:
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    llm_api_key = os.getenv("LLM_API_KEY")
    llm_base_url = os.getenv("LLM_BASE_URL")
    model_name = os.getenv("MODEL_NAME")
    system_prompt = os.getenv("SYSTEM_PROMPT")

    missing = [
        name
        for name, value in [
            ("TELEGRAM_TOKEN", telegram_token),
            ("LLM_API_KEY", llm_api_key),
            ("LLM_BASE_URL", llm_base_url),
            ("MODEL_NAME", model_name),
            ("SYSTEM_PROMPT", system_prompt),
        ]
        if not value
    ]
    if missing:
        raise RuntimeError(f"Missing env vars: {', '.join(missing)}")

    log_level = os.getenv("LOG_LEVEL", "INFO")

    return {
        "TELEGRAM_TOKEN": telegram_token,
        "LLM_API_KEY": llm_api_key,
        "LLM_BASE_URL": llm_base_url,
        "MODEL_NAME": model_name,
        "SYSTEM_PROMPT": system_prompt,
        "LOG_LEVEL": log_level,
    }
