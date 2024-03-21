from aiogram import types
from bot_setup import dp, bot
from states import ChatGPTState
from openai_api import get_chatgpt_response
from aiogram.dispatcher import FSMContext
from keyboards import *

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, {}! Я бот для создания тренировок с помощью ИИ".format(message.from_user.first_name),
                        reply_markup=create_reply_keyboard())
    await message.answer('Выберите группу мышц которую хотите тренировать:', reply_markup=muscles_keyboard())


@dp.message_handler()
async def process_button(message: types.Message):
    # это нужно почистить
    if message.text == "Поздороваться":
        await message.answer("Привеет.. Спасибо что читаешь статью!")
    elif message.text == "Задать вопрос":
        await message.answer("Задай мне вопрос")
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

#эти два хендлера пока не работают нормально

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!', reply_markup=muscles_keyboard())
    # await callback_query.message.delete_reply_markup()


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата вторая кнопка!')


@dp.message_handler(state=ChatGPTState.question)
async def handle_chatgpt_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text

    response = get_chatgpt_response(message.text)

    await message.answer(response.choices[0].text.strip())
    await state.finish()