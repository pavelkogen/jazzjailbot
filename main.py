from dotenv import load_dotenv
import os
import logging

from aiogram import Bot, Dispatcher, executor, types


load_dotenv()
BOT_TOKEN = os.getenv('bot_token')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(regexp='(.*лови джаза.*)')
async def start_cmd_handler(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id in [32194564]:  # list of telegram user_id who can catch Jazz

        await bot.send_message(
            chat_id=chat_id,
            text="Я ловлю Джаза",
        )
        await bot.send_sticker(
            chat_id=chat_id,
            sticker="CAACAgIAAxkBAAM1YmQPiVssRBYm3M6V5SUNdA3vAa0AAr4AA8xw_wI-r-Kv4bOZGyQE",
        )
        await bot.send_message(
            chat_id=chat_id,
            text="Ха-ха, смотрите какой он недовольный!",
        )
        await bot.send_sticker(
            chat_id=chat_id,
            sticker="CAACAgIAAxkBAAM3YmQPiakDxgEAASrN1ZmDg4oZVx7nAAIFAAMjIgQGKzmFbmd4TW4kBA",
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
