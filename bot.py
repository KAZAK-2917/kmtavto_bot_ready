import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv('TOKEN')
TARGET_CHAT = os.getenv('TARGET_CHAT')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет! Я — бот КМТAVTO 🚗\n"
        "Отправьте, пожалуйста, заявку в формате:\n\n"
        "1. ФИО\n"
        "2. Марка, модель и год авто\n"
        "3. VIN номер\n"
        "4. Что нужно подобрать (запчасти, масла и т.д.)\n"
        "5. Оригинал или аналог?\n"
        "6. Комментарии\n\n"
        "Я передам всё специалисту КМТAVTO 👨‍🔧"
    )

@dp.message_handler()
async def forward_to_admin(message: types.Message):
    await bot.send_message(TARGET_CHAT, f"📥 Заявка от {message.from_user.full_name} (@{message.from_user.username}):\n\n{message.text}")
    await message.answer("✅ Заявка принята! Скоро с вами свяжутся.")

if name == '__main__':
    executor.start_polling(dp)
