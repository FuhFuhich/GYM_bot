import aiogram

from bot_setup import dp

from handlers import *

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)