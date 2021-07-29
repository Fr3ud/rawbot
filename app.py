from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    # chat_id = message.chat.id
    # text = "Hello World!"
    #
    # sent_message = await bot.send_message(chat_id=chat_id, text=text)

    await bot.set_chat_title(chat_id=42, title="Title")

    sent_message = await bot.send_photo(chat_id=42,
                                        photo="https://m.media-amazon.com/images/M/MV5BM2EwMmRhMmUtMzBmMS00ZDQ3LTg4OGEtNjlkODk3ZTMxMmJlXkEyXkFqcGdeQXVyMjM5ODk1NDU@._V1_.jpg")
    print(sent_message.photo[-1].file_unique_id)


executor.start_polling(dp)
