from aiogram.types import Message, ReplyKeyboardMarkup, CallbackQuery, InputFile, MediaGroup, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Text, Command
from config import flowers1_photo, flowers2_photo, flowers3_photo, \
                    cake1_photo, cake2_photo, cake3_photo, PAYMENT_TOKEN
from main import dp, bot
from aiogram.types.message import ContentType
from keyboards import main_keyboard, back_main_keyboard, other_connection_keyboard, our_goods_keyboard, \
    flowers_keyboard, back_flowers_keyboard1, cake_keyboard, back_cake_keyboard, set_keyboard, back_set_keyboard, \
    back_flowers_keyboard2, back_flowers_keyboard3, KB
from keyboards import cd

import sqlite3

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text='Привет, чтобы вызвать меню напиши команду /menu')
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    cur.execute("""INSERT INTO users (user_id, name) VALUES (?,?)""", [message.chat.id, message.chat.first_name])
    cur.close()
    connect.commit()
    connect.close()

@dp.message_handler(Command('menu'))
async def m(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет, {0.first_name}! Ты попал в магазин Donum'.format(message.from_user))

    await bot.send_message(chat_id=message.from_user.id, text='Основное меню', reply_markup=[KB, main_keyboard])

@dp.callback_query_handler(text_contains='info')
async def info(call: CallbackQuery):
    await call.message.answer(text='Нет времени купить подарок? Мы это сделаем за вас!'
                              ' \n💐Букеты \n 🍰Сладости \n 🎁Подарочные наборы '
                              '\n 💡Идея. Сборка. Доставка. \n 📩 По вопросам и заказам в Директ',
                              reply_markup=back_main_keyboard)

@dp.callback_query_handler(text_contains='connection')
async def connection(call: CallbackQuery):
    await call.message.answer(text='Другая связь', reply_markup=other_connection_keyboard)

@dp.callback_query_handler(text_contains='goods')
async def goods(call: CallbackQuery):
    await call.message.answer(text='Наши товары', reply_markup=our_goods_keyboard)

@dp.callback_query_handler(text_contains='back_flowers_menu')
async def back_flowers_menu(call: CallbackQuery):
    await call.message.answer(text='Цветы', reply_markup=flowers_keyboard)


@dp.callback_query_handler(text_contains='back_main_menu')
async def back_main_menu(call: CallbackQuery):
    await call.message.answer(text='Основное меню', reply_markup=main_keyboard)


@dp.callback_query_handler(Text(equals=['flowers1', 'flowers2', 'flowers3', 'flowers']))
async def flowers(call: CallbackQuery):
    if call.data == 'flowers':
        await call.message.answer(text='Цветы', reply_markup=flowers_keyboard)

    elif call.data == 'flowers1':

        await call.message.answer_photo(caption='букет1, цена:2300', reply_markup=back_flowers_keyboard1,photo=flowers1_photo)

    elif call.data == 'flowers2':
        await call.message.answer_photo(caption='букет2, цена:2000', reply_markup=back_flowers_keyboard2, photo=flowers2_photo)

    elif call.data == 'flowers3':
        await call.message.answer_photo(caption='букет3, цена:1200', reply_markup=back_flowers_keyboard3, photo=flowers3_photo)

@dp.callback_query_handler(Text(equals=['cake1', 'cake2', 'cake3', 'cake']))
async def cake(call: CallbackQuery):
    if call.data == 'cake':
        await call.message.answer(text='Пироженные', reply_markup=cake_keyboard)

    elif call.data == 'cake1':
        await call.message.answer_photo(caption='Цена капкейков:\nСтандартный размер 150₽ штука;\nBig size 210₽ штука.',
                                        reply_markup=back_cake_keyboard,
                                        photo=cake1_photo)
    elif call.data == 'cake2':
        await call.message.answer_photo(caption='Цена капкейков:\nСтандартный размер 150₽ штука;\nBig size 210₽ штука.',
                                        reply_markup=back_cake_keyboard,
                                        photo=cake2_photo)
    elif call.data == 'cake3':
        await call.message.answer_photo(caption='Цена капкейков:\nСтандартный размер 150₽ штука;\nBig size 210₽ штука.',
                                        reply_markup=back_cake_keyboard,
                                        photo=cake3_photo)

@dp.callback_query_handler(Text(equals=['set', 'set1', 'set2']))
async def set(call: CallbackQuery):
    if call.data == 'set':
        await call.message.answer(text='Наборы', reply_markup=set_keyboard)

    elif call.data == 'set1':
        set1_album = MediaGroup()
        set1_album.attach_photo(photo=flowers1_photo)
        set1_album.attach_photo(photo=cake1_photo)
        await call.message.answer_media_group(media=set1_album)
        await call.message.answer(text='Цена набора 3700₽', reply_markup=back_set_keyboard)

    elif call.data == 'set2':
        set2_album = MediaGroup()
        set2_album.attach_photo(photo=flowers2_photo)
        set2_album.attach_photo(photo=cake2_photo)
        await call.message.answer_media_group(media=set2_album)
        await call.message.answer(text='Цена набора 2700₽', reply_markup=back_set_keyboard)

@dp.callback_query_handler(cd.filter(id=['1','2','3']))
async def add_cart(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)

    product_id = callback_data.get('id')
    user_id = call.message.chat.id

    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO cart (user_id, prosuct_id) VALUES (?, ?)""", [user_id, product_id])
    cursor.close()
    connect.commit()
    connect.close()

    await call.message.answer('Added')

@dp.message_handler(text_contains='ОПЛАТИТЬ')
async def buy_cart(message: Message):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    data = cursor.execute("""SELECT * FROM cart WHERE user_id=(?)""", [message.chat.id]).fetchall()
    cursor.close()
    connect.commit()
    cursor = connect.cursor()
    new_data = []
    for i in range(len(data)):
        new_data.append(cursor.execute("""SELECT * FROM products WHERE id=(?)""", [data[i][1]]).fetchall())
    cursor.close()
    connect.commit()
    connect.close()
    new_data = [new_data[i][0] for i in range(len(new_data))]
    prices = [LabeledPrice(label=i[1], amount=i[2]) for i in new_data]
    if len(new_data) == 0:
        await bot.send_message(message.chat.id, 'Ваша корзина пуста')
    else:
        await bot.send_invoice(message.chat.id,
                               title='Cart',
                               description='Description',
                               provider_token=PAYMENT_TOKEN,
                               currency='rub',
                               need_email=True,
                               prices=prices,
                               start_parameter='example',
                               payload='some_invoice')

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)



@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def s_pay(message: Message):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("""DELETE FROM cart WHERE user_id=(?)""", [message.chat.id])
    cursor.close()
    connect.commit()
    connect.close()
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!')

@dp.message_handler(text_contains='buy11')
async def ddf(message: Message):
    await bot.send_message(message.chat.id, 'proshlo')