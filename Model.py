import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

with open('config.json', 'r') as file:
    data = json.load(file)
    TOKEN = data.get('ii_api_key')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def create_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("👋 Поздороваться")
    button2 = KeyboardButton("❓ Задать вопрос")
    keyboard.add(button1, button2)
    return keyboard

def create_question_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Как меня зовут?")
    btn2 = KeyboardButton("Что я могу?")
    back = KeyboardButton("Вернуться в главное меню")
    keyboard.add(btn1, btn2, back)
    return keyboard

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, {}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user.first_name),
                        reply_markup=create_reply_keyboard())

@dp.message_handler()
async def process_button(message: types.Message):
    if message.text == "👋 Поздороваться":
        await message.answer("Привеет.. Спасибо что читаешь статью!")
    elif message.text == "❓ Задать вопрос":
        await message.answer("Задай мне вопрос", reply_markup=create_question_keyboard())
    elif message.text == "Как меня зовут?":
        await message.answer("У меня нет имени..")
    elif message.text == "Что я могу?":
        await message.answer("Поздороваться с читателями")
    elif message.text == "Вернуться в главное меню":
        await message.answer("Вы вернулись в главное меню", reply_markup=create_reply_keyboard())
    else:
        await message.answer("На такую комманду я не запрограммировал..")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
