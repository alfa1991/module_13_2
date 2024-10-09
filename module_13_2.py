from aiogram import Bot, Dispatcher, types
import asyncio

# Токен вашего бота
API_TOKEN = 'здесь токен'

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')

# Обработчик всех остальных сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')

# Запуск бота
async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
