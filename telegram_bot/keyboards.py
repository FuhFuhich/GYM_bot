from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def create_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Главное меню")
    keyboard.add(button1)
    return keyboard

def muscles_keyboard():
    inline_btn_1 = InlineKeyboardButton('Бицепс', callback_data='button1')
    inline_btn_2 = InlineKeyboardButton('Трицепс', callback_data='button2')
    inline_btn_3 = InlineKeyboardButton('Плечи', callback_data='button3')
    inline_btn_4 = InlineKeyboardButton('Предпечья', callback_data='button4')
    inline_btn_5 = InlineKeyboardButton('Грудь', callback_data='button5')
    inline_btn_6 = InlineKeyboardButton('Пресс', callback_data='button6')
    inline_btn_7 = InlineKeyboardButton('Спина', callback_data='button7')
    inline_btn_8 = InlineKeyboardButton('Квадрицепсы', callback_data='button8')
    inline_btn_9 = InlineKeyboardButton('Задняя поверхность бедра', callback_data='button9')
    inline_btn_10 = InlineKeyboardButton('Икроножные', callback_data='button10')
    inline_btn_11 = InlineKeyboardButton('Ягодицы', callback_data='button11')
    inline_kb_muscles = InlineKeyboardMarkup(row_width=1)
    inline_kb_muscles.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_11, inline_btn_10)
    return inline_kb_muscles



def bicep():
    inline_btn_1_bicep = InlineKeyboardButton('Упражнение 1', callback_data='button1_bicep')
    inline_btn_2_bicep = InlineKeyboardButton('Упражнение 2', callback_data='button2_bicep')
    inline_btn_3_bicep = InlineKeyboardButton('Упражнение 3', callback_data='button3_bicep')
    inline_kb_bicep = InlineKeyboardMarkup(row_width=1)
    inline_kb_bicep.add(inline_btn_1_bicep, inline_btn_2_bicep, inline_btn_3_bicep)
    return inline_kb_bicep

def deleteExercise():
    inline_btn_1_del = InlineKeyboardButton('Да', callback_data='delYes')
    inline_btn_2_del = InlineKeyboardButton('Нет', callback_data='delNo')
    inline_kb_deleteExercise = InlineKeyboardMarkup(row_width=1)
    inline_kb_deleteExercise.add(inline_btn_1_del, inline_btn_2_del)
    return inline_kb_deleteExercise
