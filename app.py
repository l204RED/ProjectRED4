async def on_startup(dp):

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Бот запущен')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)


# # from aiogram import Bot, Dispatcher, types
# # from aiogram.utils import executor
# Создаём переменную бота где Bot(token='Токен Вашего бота')
# # bot = Bot(token= '5494164709:AAEKBHgaQwPGLJaMT8cXwAcbWyJUZbXcTVY')
# Создаём диспетчер
# # dp = Dispatcher(bot)
# # @dp.message_handler() # Все сообщения
# # async def get_mesage(message: types.Message):
    # Вариант 1 -=-=-=
    # chat_id = message.chat.id
    # text = 'Ваш текст'
    # await bot.send_message(chat_id=chat_id, text=text)

    # Вариант 2 -=-=-=
    # text = 'Любой текст 123456'
    # await message.answer(text=text)

    # Вариант 3  Повторяшка -=-=-=
    # text = message.text
    # await message.answer(text=text)

    # Вариант 4  Приветствие -=-=-=
    # #     text = f"Привет {message.from_user.full_name}"
    # #    await message.answer(text=text)
# #    print(message.from_user.id, message.from_user.full_name)
    # print(message.from_user.full_name)
# # executor.start_polling(dp)