import json
import openai
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


with open('config.json', 'r') as file:
    data = json.load(file)
    TOKEN = data.get('telegram_api_key')
    openai.api_key = data.get('openai_api_key')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class ChatGPTState(StatesGroup):
    question = State()


def create_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Поздороваться")
    button2 = KeyboardButton("Задать вопрос")
    button3 = KeyboardButton("Обратиться к ИИ")
    keyboard.add(button1, button2, button3)
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
    if message.text == "Поздороваться":
        await message.answer("Привеет.. Спасибо что читаешь статью!")
    elif message.text == "Задать вопрос":
        await message.answer("Задай мне вопрос", reply_markup=create_question_keyboard())
    elif message.text == "Как меня зовут?":
        await message.answer("У меня нет имени..")
    elif message.text == "Что я могу?":
        await message.answer("Поздороваться с читателями")
    elif message.text == "Вернуться в главное меню":
        await message.answer("Вы вернулись в главное меню", reply_markup=create_reply_keyboard())
    elif message.text == "Обратиться к ИИ":
        await ChatGPTState.question.set()
        await message.answer("Задайте вопрос для ChatGPT")
    else:
        await message.answer("На такую комманду я не запрограммировал..")


@dp.message_handler(state=ChatGPTState.question)
async def handle_chatgpt_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text

    response = openai.Completion.create(
        engine="davinci",
        prompt=message.text,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.5,
    )

    await message.answer(response.choices[0].text.strip())
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
