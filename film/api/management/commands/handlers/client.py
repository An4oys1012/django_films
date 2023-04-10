from aiogram import types

from bot import dp, bot
from handlers import keyboard


# from others.db import Database

async def start(message: types.Message):
    try:
        await message.answer('Hello, dear friend!', reply_markup=keyboard.mainmenu)
    except Exception as e:
        print(e)


async def keyboard_handler(message: types.Message):
    try:
        match message.text:
            case "Comments":
                await message.reply('Do you have any suggestions or comments, '
                                    'dear?', reply_markup=keyboard.comments)
            case "Subscription":
                await message.reply('Please enter your nickname in telegram')
            case _:
                await message.answer('Thank you for your attention to our site!')
    except Exception as e:
        print(e)


async def inline_comments_buttons_handler(call: types.CallbackQuery):
    match call.data:
        case "сomment_suggestion":
            await call.message.answer("Please write your suggestions.")
            await bot.answer_callback_query(callback_query_id=call.id)
        case "сomment_admontion":
            await call.message.answer("Please write your comments. We will consider them!")
            await bot.answer_callback_query(callback_query_id=call.id)
        case _:
            await call.message.answer('Thank you for your attention to our site!')


def register_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(keyboard_handler, state=None)
    dp.register_callback_query_handler(inline_comments_buttons_handler)
