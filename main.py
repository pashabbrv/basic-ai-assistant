import asyncio

from aiogram import Bot, Dispatcher

from bot.config import get_settings
from bot.handlers import router


async def main() -> None:
    s = get_settings()
    bot = Bot(token=s["TELEGRAM_TOKEN"])
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
