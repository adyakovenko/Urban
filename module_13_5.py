from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api =''
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_calc = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
kb.add(button_calc)
kb.add(button_info)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    ok = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Нажми Рассчитать',reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) + 5 * float(data['age'])
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информации нет, нажми Рассчитать', reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)