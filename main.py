import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from bot.config import get_settings
from bot.handlers import router


async def main() -> None:
    s = get_settings()
    level = getattr(logging, s["LOG_LEVEL"].upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        stream=sys.stdout,
    )
    logger = logging.getLogger(__name__)
    logger.info("Bot starting")
    bot = Bot(token=s["TELEGRAM_TOKEN"])
    dp = Dispatcher()
    dp.include_router(router)
    logger.info("Bot started, polling")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
