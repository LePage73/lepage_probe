# Домашнее задание по теме "Клавиатура кнопок".

import logging
logging.basicConfig(level=logging.DEBUG, filemode="w", filename="log_test_13_5.log",
                        encoding="utf-8", format="%(levelname)s :< %(asctime)s >: %(message)s \n-------")

# aiogram 3.11
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State,StatesGroup
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "*****************************************************" # здесь ключ API Вашего бота
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage()) # в качестве базы данных для машины состояний ипользуем опер. память

###### ЛОГИКА #########################################

# задаем клавиатуру - настраиваемую
def kb_(*args, input_placeholder = ''):
    kb_list = []
    kb_list.append([types.KeyboardButton(text=str(x)) for x in args])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, input_field_placeholder=input_placeholder)
    return keyboard

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = ''

def miffline_san_jeor(data):
    try:
        if UserState.gender == 'male':
            return (10 * int(data['weigth'])
                    + 6.25 * int(data['growth'])
                    + 5 * int(data['age'])
                    + 5)
        else:
            return (10 * int(data['weigth'])
                    + 6.25 * int(data['growth'])
                    + 5 * int(data['age'])
                    -161)
    except:
        return ' - ERROR -'

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

###### БЛОК ХЭНДЛЕРОВ #################################

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message,state: FSMContext):
    kb = kb_('Рассчитать', 'Информация', input_placeholder='Рассчитать?')
    await message.answer("Привет! Я тестовый бот помогающий твоему здоровью\n "
                         "Я могу рассчитать количество калорий для Вас", reply_markup=kb)

@dp.message(F.text == 'Рассчитать')
async def calc_start(message: types.Message, state: FSMContext):
    await state.clear()
    kb = kb_('Мужчина', 'Женщина', 'Сброс', input_placeholder='Укажите Ваш пол')
    await message.answer("Укажите Ваш пол", reply_markup=kb)

@dp.message(F.text == 'Информация')
async def info(message: types.Message, state: FSMContext):
    await state.clear()
    kb = kb_('Рассчитать', 'Информация', input_placeholder='Рассчитать?')
    await message.answer("Привет! Я тестовый бот помогающий твоему здоровью\n "
                         "Я могу рассчитать количество калорий для Вас", reply_markup=kb)

@dp.message(F.text == "Мужчина")
async def set_age(message: types.Message, state: FSMContext):
    UserState.gender = 'male'
    kb = types.ReplyKeyboardRemove()
    await message.reply("Сколько Вам лет?", reply_markup=kb)
    await state.set_state(UserState.age)

@dp.message(F.text == "Женщина")
async def set_age(message: types.Message, state: FSMContext):
    UserState.gender = 'female'
    kb = types.ReplyKeyboardRemove()
    await message.reply("Сколько Вам лет?", reply_markup=kb)
    await state.set_state(UserState.age)

@dp.message(F.text, UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age = message.text)
    await message.answer("Каков Ваш рост?")
    await state.set_state(UserState.growth)

@dp.message(F.text, UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth = message.text)
    await message.answer("Каков Ваш вес?")
    await state.set_state(UserState.weight)

@dp.message(F.text, UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weigth = message.text)
    data = await state.get_data()
    calories = miffline_san_jeor(data)
    await message.answer(f'Рекомендуемое Вам количество калорий: {calories} в день')
    await state.clear()

@dp.message(F.text == 'Сброс')
async def reset_(message, state: FSMContext):
        kb = types.ReplyKeyboardRemove()
        await message.reply("Введите команду /start", reply_markup=kb)
        await state.clear()
@dp.message()
async def all_message(message):
        await message.reply("Не понял...\nВведите команду /start")


########################################################
if __name__ == "__main__":
    print("Поехали")
    asyncio.run(main())