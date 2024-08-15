#Домашнее задание по теме "Машина состояний".

import logging
logging.basicConfig(level=logging.DEBUG, filemode="w", filename="log_test_13_4.log",
                        encoding="utf-8", format="%(levelname)s :< %(asctime)s >: %(message)s \n-------")

# aiogram 3.11
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State,StatesGroup
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
import asyncio

api = "**********************************************" # здесь ключ API Вашего бота
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage()) # в качестве базы данных для машины состояний ипользуем опер. память

###### ЛОГИКА #########################################
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def miffline_san_jeor(data):
    try:
        return (10 * int(data['weigth'])
                + 6.25 * int(data['growth'])
                + 5 * int(data['age'])
                + 5)
    except:
        return ' - ERROR -'

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    #logging.info("Стартанули")


###### БЛОК ХЭНДЛЕРОВ #################################

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я тестовый бот помогающий твоему здоровью")
@dp.message(F.text == "калорий")
async def set_age(message: types.Message, state: FSMContext):
    await message.reply("Сколько Вам лет?")
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
@dp.message()
async def all_message(message):
        await message.reply("Не понял...")

########################################################
if __name__ == "__main__":
    print("Поехали")
    asyncio.run(main())