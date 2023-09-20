import logging
from aiogram import Bot, Dispatcher, executor, types
import random
import json
from aiogram.types import InlineKeyboardButton as in_kb
from keyboards.inline import first
from keyboards.default import phone, geolocation
# Configure logging
from utils.set_bot_commands import set_default_commands

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token="TOKEN")
dp = Dispatcher(bot)

is_echo = False


@dp.message_handler(commands=["start"])
async def welcome(message:types.Message):
    
    await message.answer(
        'Welcome',
        reply_markup=phone
    )
    
@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_receive(message:types.Message):
    print(message.from_user.id == message.contact.user_id)
    print(message.contact.phone_number)    

@dp.message_handler(commands=["geo"])
async def request_geo(message:types.Message):
    print(message.from_user)
    await message.answer(
        'Welcome',
        reply_markup=geolocation
    )
    
@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def geo_receive(message:types.Message):
    print(message.location)
    # print(message.contact.phone_number)    
    
@dp.message_handler(commands=["showbtn"])
async def show(message:types.Message):
    await message.answer(
        'Press the button',
        reply_markup=first
    )

@dp.callback_query_handler(text='second')
async def second_step(call: types.CallbackQuery):
    await call.message.answer('You pressed the button!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)