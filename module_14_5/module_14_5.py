import asyncio

import aiogram
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types import FSInputFile
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State

import crud_functions


# databases
# product database
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price if price is not None else 0
        self.description = description if description is not None else 'Без описания'


crud_functions.initiate_dbs()
crud_functions.add_products([
    Product('red', 10, 'красная таблетка'),
    Product('green', 20, 'зеленая таблетка'),
    Product('blue', 30, 'синяя таблетка'),
    Product('yellow', 90, 'желтая таблетка')
])

# main bot setup
api = ''
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(storage=aiogram.fsm.storage.memory.MemoryStorage())

# keyboards
kb_main = ReplyKeyboardBuilder(markup=[
    [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')],
    [KeyboardButton(text='Регистрация')]
]).as_markup(resize_keyboard=True)

kb_calories = InlineKeyboardBuilder(markup=[
    [InlineKeyboardButton(text='Рассчитать формулу калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
]).as_markup(resize_keyboard=True)

names = crud_functions.get_products_names()
buttons = []
for name in names:
    buttons.append([InlineKeyboardButton(text=name, callback_data='product_buying')])
kb_buying = InlineKeyboardBuilder(markup=buttons).as_markup(resize_keyboard=True)


# states
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    ok = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


# commands
@dp.message(Command('start'))
async def test(message):
    await message.answer('Нажмите рассчитать', reply_markup=kb_main)


# kb main
@dp.message(F.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_calories)


@dp.message(F.text == 'Информация')
async def info(message):
    await message.answer('Пожалуйста, не нажимайте эту кнопку.', reply_markup=kb_main)


@dp.message(F.text == 'Купить')
async def buy_medicine(message):
    products = crud_functions.get_all_products()
    names = crud_functions.get_products_names()
    for i in range(len(products)):
        img = FSInputFile(f'files/{names[i]}.png')
        await message.answer_photo(img, products[i])
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_buying)


# kb calories
@dp.callback_query(F.data == 'calories')
async def respond_calories(call, state):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await state.set_state(UserState.age)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call):
    await call.message.answer(f'Для мужчин: (10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5) * активность\nДля женщин: (10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161) * активность')
    await call.answer()


# fsm calories
@dp.message(UserState.age)
async def process_age(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def process_growth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def process_growth(message, state):
    await state.update_data(weight=message.text)
    data = await state.update_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) + 5 * float(data['age'])
    await message.answer(f'Ваша норма калорий {calories}')


# fsm registration
@dp.message(F.text == 'Регистрация')
async def sign_up(message, state):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message, state):
    if crud_functions.is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await sign_up(message, state)
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.update_data()
    crud_functions.add_user(data['username'], data['email'], int(data['age']))
    await message.answer('Регистрация прошла успешно')


# product buying
@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
