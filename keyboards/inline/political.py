from aiogram.utils.keyboard import InlineKeyboardBuilder
from parsing import pars


builder = InlineKeyboardBuilder()

async def getKeyboard (): 
    #заголовки новин з парсингу
    temp_data = pars()
    for item in temp_data :
        item getheader
        item.get('header')
