from aiogram import Bot, Dispatcher
from config import load_config

config = load_config()

bot = Bot(token=config.get('telegram_api_key'))
dp = Dispatcher(bot)
