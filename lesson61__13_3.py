# aiogram 3.11
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

api = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # здесь ключ API Вашего бота
bot = Bot(token=api)
dp = Dispatcher()


# dp = Dispatcher(bot, storage=MemoryStorage()) # Это в aiogram 2.25.1 было сйчас не работает
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates = True)     # Это в aiogram 2.25.1 было сйчас не работает

###### ЛОГИКА #########################################
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


###### БЛОК ХЭНДЛЕРОВ #################################
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я тестовый бот помогающий твоему здоровью")

# Хендлер на все сообщения, после него мессаги не пройдут
@dp.message()
async def all_message(message):
    await message.reply("Введите команду /start, чтобы начать общение.")


####### ДАЛЬШЕ ХЭНДЛЕРЫ /ОБРАБОТЧИКИ/ НЕ СРАБОТАЮТ #####
# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


########################################################
if __name__ == "__main__":
    asyncio.run(main())


