import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# Токен из настроек Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        f"Теперь я работаю стабильно и не отключаюсь!\n\n"
        f"Твой Telegram ID: `{message.from_user.id}`",
        parse_mode="Markdown"
    )

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"🤖 Ты написал: {message.text}")

# --- Веб-сервер для обмана Render ---
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render автоматически передает номер порта в переменную PORT
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Веб-сервер запущен на порту {port}")

# --- Главная функция запуска ---
async def main():
    # Запускаем веб-сервер в фоне
    await start_web_server()
    print("Бот успешно запущен и готов к работе!")
    # Запускаем чтение сообщений Telegram
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
