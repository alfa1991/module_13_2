import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import logging

# Токен вашего бота
API_TOKEN = '7707735615:AAGTv-6x0mrzo4wf8svUoJBPRNzCLA9r24Y'

# Настраиваем логирование (опционально)
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token=API_TOKEN)

# Создаем объект диспетчера
dp = Dispatcher()

# Создаем объект роутера
router = Router()


# Обработчик команды /start
@router.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


# Обработчик всех остальных сообщений
@router.message()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


# Функция для правильного завершения работы бота
async def shutdown(dispatcher: Dispatcher):
    await bot.session.close()  # Закрываем сессию бота


# Основная функция
async def main():
    # Включаем роутер в диспетчер
    dp.include_router(router)

    # Запуск polling
    try:
        await dp.start_polling(bot)
    finally:
        await shutdown(dp)  # Закрываем ресурсы при завершении


if __name__ == '__main__':
    try:
        # Запускаем приложение
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен.")
