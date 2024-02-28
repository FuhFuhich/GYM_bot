from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "6722307971:AAFP8FBm6eDMweDxUOBcJxtGGzojVZ5ZNBE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    if msg.text == '/start':
        await msg.reply(f"Я бот. Приятно познакомиться, {msg.from_user.first_name}")
    elif msg.text == '/help':
        await msg.reply(f"список команд:\n"
                        f"1. Привет\n")


# @dp.message_handler()
# async def send_to_openai(msg: types.Message):
#     # Реализация отправки сообщения ИИ


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю, что это значит.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
