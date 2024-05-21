from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('фото')
    button_2 = KeyboardButton('клава')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('фото собаки')
    button_4 = KeyboardButton('назад клава')
    keyboard_2.add(button_3, button_4)
    return keyboard_2
