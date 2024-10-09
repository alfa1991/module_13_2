# module_13_2
Хендлеры обработки сообщений/Message Handling Handlers

Пример старого подхода (aiogram 2.x)
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Токен вашего бота
API_TOKEN = 'ваш токен здесь'

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет! Я бот, помогающий твоему здоровью.')

# Обработчик всех остальных сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.reply('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

  
  Пример нового подхода (aiogram 3.x)
  import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import logging

# Токен вашего бота
API_TOKEN = 'ваш токен здесь'

# Настраиваем логирование
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

# Основная функция
async def main():
    dp.include_router(router)  # Включаем роутер в диспетчер
    await dp.start_polling(bot)  # Запуск polling

if __name__ == '__main__':
    asyncio.run(main())


Основные отличия:
Использование маршрутизаторов:

В новой версии используется Router, который позволяет группировать обработчики по логическим единицам. Это делает код более структурированным и понятным.
Декораторы:

В старой версии для регистрации обработчиков использовались декораторы, такие как @dp.message_handler(). В новой версии используется @router.message(), что указывает на то, что обработчик принадлежит определённому маршрутизатору.
Запуск:

В старой версии запуск бота осуществлялся через executor.start_polling(dp), а в новой версии используется await dp.start_polling(bot) внутри асинхронной функции main().
