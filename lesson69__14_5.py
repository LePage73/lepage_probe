# Домашнее задание по теме "Написание примитивной ORM"

import logging
logging.basicConfig(level=logging.DEBUG, filemode="w", filename="log_test_14_5.log",
                        encoding="utf-8", format="%(levelname)s :< %(asctime)s >: %(message)s \n-------")

# aiogram 3.11
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

###### импортируем свои ############################################################################
import crud_functions as crud

api = "7286687702:AAEhBOCaxfd_0P3ubdbMRk7cOsIVGRyXsLo" # здесь ключ API Вашего бота
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage()) # в качестве базы данных для машины состояний ипользуем опер. память

###### ЛОГИКА #########################################

# задаем клавиатуру - настраиваемую
def kb_(*args, input_placeholder = ''):
    kb_list = []
    for x in args:
        kb_list.append([KeyboardButton(text=str(x))])
    print(kb_list)
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, input_field_placeholder=input_placeholder)
    return keyboard

# задаем инлайн клавиатуру
def kb_inline(*args, columns = 1):
    builder = InlineKeyboardBuilder()
    for x in args:
        builder.add(InlineKeyboardButton(text=str(x).split(':')[1], callback_data=str(x).split(':')[0]))
    builder.adjust(columns)
    return builder.as_markup(resize_keyboard=True)

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
async def cmd_start(message: types.Message, state: FSMContext):
    kb = kb_('Рассчитать', 'Информация', 'Регистрация', 'Купить', input_placeholder='Рассчитать?')
    await message.answer("Привет! Я тестовый бот помогающий твоему здоровью\n "
                         "Я могу рассчитать количество калорий для Вас", reply_markup=kb)

@dp.message(F.text == 'Рассчитать')
async def calc_start(message: types.Message, state: FSMContext):
    await state.clear()
    kb = kb_inline('calories: Рассчитать норму калорий', 'formulas: Формулы рассчета', columns=1)
    await message.answer("Выберите опцию", reply_markup=kb)

@dp.callback_query(F.data == 'formulas')
async def get_formulas(call):
    await call.message.answer("Формула расчета калорий для мужчин:\n"
                              "10 х Вес (кг) + 6.25 х Рост (см) + 5 х Возраст (лет) + 5\n"
                              "Для женщин:\n"
                              "10 х Вес (кг) + 6.25 х Рост (см) + 5 х Возраст (лет) - 161")
    await call.answer()

@dp.message(F.text == 'Информация')
async def info(message: types.Message, state: FSMContext):
    await state.clear()
    kb = kb_('Рассчитать', 'Информация', input_placeholder='Рассчитать?')
    await message.answer("Привет! Я тестовый бот помогающий твоему здоровью\n "
                         "Я могу рассчитать количество калорий для Вас", reply_markup=kb)

@dp.callback_query(F.data == 'calories')
async def calc_start(call):
    kb = kb_inline('male: Мужчина', 'female: Женщина',  columns=2)
    await call.message.answer("Укажите Ваш пол", reply_markup=kb)
    await call.answer()


@dp.callback_query(F.data == "male")
async def set_age(call, state: FSMContext):
    UserState.gender = 'male'
    kb = types.ReplyKeyboardRemove()
    await call.message.answer("Сколько Вам лет?", reply_markup=kb)
    await state.set_state(UserState.age)
    await call.answer()

@dp.callback_query(F.data == "female")
async def set_age(call, state: FSMContext):
    UserState.gender = 'female'
    kb = types.ReplyKeyboardRemove()
    await call.message.answer("Сколько Вам лет?", reply_markup=kb)
    await state.set_state(UserState.age)
    await call.answer()

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

@dp.message(F.text == "Купить")
async def get_buying_list(message: types.Message):
    kb = kb_inline('product_buying: Product1',
                   'product_buying: Product2',
                   'product_buying: Product3',
                   'product_buying: Product4',
                   columns=4)
    for str_ in all_products:
        file_name_ = str_[3]
        await message.answer(f'Название: {str_[1]} | Описание: {str_[2]} | Цена: {str_[4]} ')
        await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile(file_name_))
    await message.answer('Выберите продукт для покупки:', reply_markup=kb)

@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call):
    kb = types.ReplyKeyboardRemove()
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=kb )
    await call.answer()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()
@dp.message(F.text == "Регистрация")
async def sign_up(message: types.Message, state: FSMContext):
    print('Registration')
    await state.clear()
    kb = ReplyKeyboardRemove()
    await message.answer('Введите Ваше имя (латинскими буквами)', reply_markup=kb)
    await state.set_state(RegistrationState.username)
@dp.message(F.text, RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    print('UserName')
    if crud.is_included(message.text):
        await message.answer('Такой пользователь существует!\nВведите другое имя')
        await state.set_state(RegistrationState.username)
    else:
        RegistrationState.username = str(message.text)
        await message.answer('Введите свой E-mail')
        await state.set_state(RegistrationState.email)
@dp.message(F.text, RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    print('E-mail')
    RegistrationState.email = message.text
    await message.answer('Укажите свой возраст')
    await state.set_state(RegistrationState.age)

@dp.message(F.text, RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    print('Age')
    RegistrationState.age = message.text
    crud.add_user(RegistrationState.username,RegistrationState.email,RegistrationState.age)
    await message.answer('Регистрация прошла успешно')
    await state.clear()





########################################################
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
    all_products = crud.get_all_products()
    asyncio.run(main())