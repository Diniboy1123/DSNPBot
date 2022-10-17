import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types

import config

API_TOKEN = config.token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Hi!\nI'm a Disney+ information grabber bot! If you want to know which series are available at a specific region, this bot is for you!"
    )

if __name__ == '__main__':
    bot.logging = logging.getLogger()
    executor.start_polling(dp, skip_updates=True)
