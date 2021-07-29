from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Hello World!"

    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())

executor.start_polling(dp)
