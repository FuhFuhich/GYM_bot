from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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
