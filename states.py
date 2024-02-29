from aiogram.dispatcher.filters.state import State, StatesGroup


class ChatGPTState(StatesGroup):
    question = State()
