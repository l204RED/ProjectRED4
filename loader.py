from aiogram import Bot, types, Dispatcher

from data import config

# Создаём переменную бота где Bot(token='Токен Вашего бота')
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Создаём диспетчер
dp = Dispatcher(bot)