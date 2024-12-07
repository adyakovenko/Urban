from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7867946561:AAF1Xf1spXQMIulTspGN4oSPl4oQ0kcbqh4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# data
class Product:
    def __init__(self, name, price=None, comment=None, path_picture=None):
        self.name = name
        self.price = price if price is not None else 'Бесценна'
        self.comment = comment if comment is not None else 'Без описания'
        self.picture_name = path_picture if path_picture is not None else f'{name}.png'

products = []
products.append(Product('red', 10, 'красная таблетка'))
products.append(Product('green', 20, 'зеленая таблетка'))
products.append(Product('blue', 30, 'синяя таблетка'))
products.append(Product('yellow', None, 'желтая таблетка'))

# keyboards
kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True)

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
button_calc = InlineKeyboardButton('Рассчитать формулу калорий', callback_data='calories')
button_form = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb_inline.add(button_calc)
kb_inline.add(button_form)

kb_buying = InlineKeyboardMarkup(resize_keyboard=True)
for product in products:
    kb_buying.add(InlineKeyboardButton(product.name, callback_data='product_buying'))

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    ok = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Нажми Рассчитать', reply_markup=kb_main)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer(f'Для мужчин: (10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5) * активность\nДля женщин: (10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161) * активность')
    await call.answer()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for product in products:
        with open(f'files/{product.picture_name}', 'rb') as img:
            await message.answer_photo(img, f'Название: {product.name} | Описание: {product.comment} | Цена: {product.price}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_buying)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
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
    await message.answer('Информации нет, нажми Рассчитать', reply_markup=kb_main)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)