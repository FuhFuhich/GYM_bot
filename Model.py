from aiogram import Bot, types, Dispatcher, executor
from random import randint
import openai

TOKEN = "6722307971:AAFP8FBm6eDMweDxUOBcJxtGGzojVZ5ZNBE"
OPENAI_API_TOKEN = "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"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    if msg.text == '/start':
        await msg.reply(f"Я бот. Приятно познакомиться, {msg.from_user.first_name}")
    elif msg.text == '/help':
        await msg.reply(f"список команд:\n"
                        f"1. Привет\n"
                        f"2. Иди нахуй\n"
                        f"3. Артем\n"
                        f"4. Илья\n"
                        f"5. Настя\n"
                        f"6. Зиг\n"
                        f"7. Хуй\n"
                        f"8. Казик\n")



@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')

   elif msg.text.lower() == 'chat gpt':
       await msg.answer('Добро пожаловать в chat GPT!\nВведите сообщение end для выхода из chat GPT')
       while True:
           user_input = (await bot.wait_for('message', timeout=3.0)).text.lower()
           if user_input == 'end':
               await msg.answer('До свидания! Выход из чата GPT.')
               break
           else:
               response = openai.Completion.create(
                   engine="text-davinci-003",
                   prompt=msg.text,
                   max_tokens=100
               )
               gpt_response = response.choices[0].text.strip()
               await msg.answer(f'GPT ответ: {gpt_response}')
               response = "GPT ответ: " + user_input  # Replace this line with actual GPT interaction
               await msg.answer(response)
   elif msg.text.lower() == 'иди нахуй':
       await msg.answer('Сам пошел!')
   elif msg.text.lower() == 'артем':
       await msg.answer('старый')
   elif msg.text.lower() == 'настя':
       await msg.answer('альтушка!')
   elif msg.text.lower() == "илья":
       await msg.answer('Солнышко!')
   elif msg.text.lower() == "зиг":
       await msg.answer('ХАИЛЬ!')
   elif msg.text.lower() == 'хуй':
       a = randint(0,100)
       if a > 50:
           await msg.answer('ух ты, вот это размерчик, как у насти берчик ' + str(a) + "см")
       elif a < 20:
           await msg.answer('слабо-слабо ' + str(a) + "см")
       else:
           await msg.answer('нормуль ' + str(a) + "см")
   elif msg.text.lower() == "казик":
       await msg.answer(randint(0, 100))
   else:
       await msg.answer('Не понимаю, что это значит.')


if __name__ == '__main__':
   executor.start_polling(dp)