from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.llm import ask_llm

router = Router()
_history: dict[int, list[dict]] = {}


def _get_history(user_id: int) -> list[dict]:
    return _history.setdefault(user_id, [])


@router.message(Command("start"))
async def start(message: Message) -> None:
    _history[message.from_user.id] = []
    await message.answer("Привет! Напиши сообщение — я отвечу через модель.")


@router.message(F.text)
async def on_text(message: Message) -> None:
    user_id = message.from_user.id
    history = _get_history(user_id)

    reply = await ask_llm(history=history, message=message.text)

    history.append({"role": "user", "content": message.text})
    history.append({"role": "assistant", "content": reply})

    await message.answer(reply or "(пустой ответ)")
