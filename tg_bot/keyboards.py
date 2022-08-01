from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from config import url_inst, url_maria, url_yana
from aiogram.utils.callback_data import CallbackData

cd = CallbackData('buy', 'id')


main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Информация о нас', callback_data='info'),
            InlineKeyboardButton(text='Другая связь', callback_data='connection')
        ],
        [
            InlineKeyboardButton(text='Наши товары', callback_data='goods')
        ],
        [
            InlineKeyboardButton(text='Оплатить корзину', callback_data='buy_cart')
        ]
    ]
)

back_main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ]
    ]
)

back_flowers_keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back_flowers_menu'),
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ],
        [
            InlineKeyboardButton('Добавить в корзину', callback_data='buy:1')
        ]
    ]
)
other_connection_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Наш инстаграм', url=url_inst)
        ],
        [
            InlineKeyboardButton(text='Админ Мария', url=url_maria),
            InlineKeyboardButton(text='Админ Яна', url=url_yana)
        ],
        [
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ]
    ]
)

our_goods_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Цветы', callback_data='flowers'),
            InlineKeyboardButton(text='Пироженное', callback_data='cake'),
        ],
        [
            InlineKeyboardButton(text='Подарочный набор', callback_data='set')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_main_menu')
        ]
    ]
)

flowers_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Букет №1: 2300rub', callback_data='flowers1'),
            InlineKeyboardButton(text='Букет №2: 2000rub', callback_data='flowers2'),
            InlineKeyboardButton(text='Букет №3: 12000rub', callback_data='flowers3')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='goods'),
        ]
    ]
)

cake_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пироженное №1', callback_data='cake1'),
            InlineKeyboardButton(text='Пироженное №2', callback_data='cake2'),
            InlineKeyboardButton(text='Пироженное №3', callback_data='cake3')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='goods')
        ]
    ]
)

back_cake_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='cake'),
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ]
    ]
)

set_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Набор №1', callback_data='set1'),
            InlineKeyboardButton(text='Набор №2', callback_data='set2')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='goods')
        ]
    ]
)

back_set_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='set'),
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ]
    ]
)

back_flowers_keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back_flowers_menu'),
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ],
        [
            InlineKeyboardButton('Добавить в корзину', callback_data='buy:2')
        ]
    ]
)
back_flowers_keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back_flowers_menu'),
            InlineKeyboardButton(text='На главную', callback_data='back_main_menu')
        ],
        [
            InlineKeyboardButton('Добавить в корзину', callback_data='buy:3')
        ]
    ]
)

buy_cart_keyboard = KeyboardButton('ОПЛАТИТЬ')
KB = ReplyKeyboardMarkup()
KB.add(buy_cart_keyboard)
