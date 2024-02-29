from aiogram import types
from bot_setup import dp
from states import ChatGPTState
from keyboards import create_reply_keyboard, create_question_keyboard
from openai_api import get_chatgpt_response
from aiogram.dispatcher import FSMContext


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

    response = get_chatgpt_response(message.text)

    await message.answer(response.choices[0].text.strip())
    await state.finish()