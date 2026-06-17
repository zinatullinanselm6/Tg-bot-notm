import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Render автоматически подставит токен из настроек, которые мы укажем позже
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        f"Я твой первый тестовый бот, запущенный на хостинге Render!\n\n"
        f"Твой Telegram ID: `{message.from_user.id}`\n"
        f"Отправь мне любое сообщение, и я повторю его.",
        parse_mode="Markdown"
    )

@dp.message()
async def echo_message(message: types.Message):
    # Бот просто отправляет назад то же самое сообщение
    await message.answer(f"🤖 Ты написал: {message.text}")

async def main():
    print("Бот успешно запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
