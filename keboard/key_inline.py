from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inlin = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('посмотреть', url='https://www.youtube.com/watch?v=rJ70eUikBZk&list=PLBxD0UwW2SxmiogBXtVv5kItQXXQaPPKh&index=6')
    but_inline2 = InlineKeyboardButton('посмотреть', url='https://www.youtube.com/watch?v=rJ70eUikBZk&list=PLBxD0UwW2SxmiogBXtVv5kItQXXQaPPKh&index=6')
    keyboard_inlin.add(but_inline, but_inline2)
    return keyboard_inlin
