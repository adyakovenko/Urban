from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command('start'))
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())