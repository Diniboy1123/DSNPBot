import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types

from disney import DisneyPlus
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

@dp.message_handler(commands=["regions"])
async def send_regions(message: types.Message):
    """
    This handler will be called when user sends `/regions` command
    """
    await message.reply(
        f"Here are the regions available ({len(bot.disney.regions)}): " + ", ".join(bot.disney.regions)
    )

if __name__ == '__main__':
    bot.logging = logging.getLogger()
    bot.disney = DisneyPlus(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=bot.disney.init_session)
