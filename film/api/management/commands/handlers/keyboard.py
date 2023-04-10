from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup

mainmenu_subscription = KeyboardButton('Subscription')
mainmenu_сomments = KeyboardButton('Comments')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenu_subscription, mainmenu_сomments)

comments = InlineKeyboardMarkup(row_width=2)
сomment_suggestion = InlineKeyboardButton(text='Suggestion', callback_data='сomment_suggestion')
сomment_admontion = InlineKeyboardButton(text='Admontion', callback_data='сomment_admontion')

comments.insert(сomment_suggestion)
comments.insert(сomment_admontion)
