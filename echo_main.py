"""
Bu aks-sado qaytaruvchi bot.
Bu botga yozilgan har bir gapni unga aks-sado singari qaytarib beradi.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API_TOKEN ni shuyerga qo\'yasiz.'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Qachonki foydalanuvchi botga 'start' va 'help' kamandasini bosganda send_welcome() funksiyasi ishlaydi.
    """
    await message.reply("Salom!\nMen aks-sado qaytaruvchi botman!\nMen sizni har bir aytgan so'zingizni qayataraman. \n\n😃 Boshladik!")

@dp.message_handler()
async def echo(message: types.Message):
    # Eski stil:  bot.send_message(message.chat.id, message.text)
    # Yangi stil : await message.answer(message.text)
    # tenglik await = bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)