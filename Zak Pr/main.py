from aiogram import Dispatcher, executor, Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from messages import *
from keyboards import *
import json, uuid,requests
from db import *



bot = Bot("")
dp = Dispatcher(bot)

price: int
btcprice: float
pricepercent: int
number = 239692
code = str(uuid.uuid4().hex[:10]).upper()

async def on_startup(_):
    await conn()
    print('Connecting to db was completed')

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.message):
    user = msg.from_user
    username = user.first_name
    user_id = msg.from_user.id
    user_login = msg.from_user.username
    user_name = msg.from_user.first_name
    cursor.execute(f"INSERT INTO users (id, login, name) VALUES ({user_id}, '{user_login}', '{user_name}')")
    conn.commit()
    await msg.answer('Боты ☯️ сайты ⚡️odium.co')
    await bot.send_message(chat_id=msg.chat.id,
                            text =f'*{username}* {START_MES}',
                            reply_markup = start_kb,
                            parse_mode='markdown')
    
#/////////////////////////////////////////////////////////////////CITYS

@dp.callback_query_handler(lambda c: c.data.startswith('nov_maj'))
async def maj_cmd(callback_query: CallbackQuery):
    global city
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Новое Мажарово (Харьковская обл.)* 🌳. Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = nov_maj_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('verhdnepr'))
async def verhdnepr_cmd(callback_query: CallbackQuery):
    global city
    city = 'Верхнеднепровск 🆕'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Верхнеднепровск* 🆕 . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = verhdnepr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('sinelnikovo'))
async def sinelnikovo_cmd(callback_query: CallbackQuery):
    global city
    city = 'Синельниково 🌾'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Синельниково* 🌾 . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = sinelnik_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pavlograd'))
async def pavlograd_cmd(callback_query: CallbackQuery):
    global city
    city = 'Павлоград ⛏'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Павлоград* ⛏ . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = pavlograd_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('kamenskoe'))
async def kamenskoe_cmd(callback_query: CallbackQuery):
    global city
    city = 'Каменско́е (Днепродзержинск) 🏭'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Каменско́е (Днепродзержинск) *🏭  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = kamenskoe_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('dnepr'))
async def dnepr_cmd(callback_query: CallbackQuery):
    global city
    city = 'Днепр 🏙 '
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Днепр* 🏙  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = dnepr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pereshepino'))
async def pereshepino_cmd(callback_query: CallbackQuery):
    global city
    city = 'Перещепино 🌳'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Перещепино *🌳  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = pereshepino_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('kremenchug'))
async def kremenchug_cmd(callback_query: CallbackQuery):
    global city
    city = 'Кременчуг 🌉'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Кременчуг *🌉  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = kremenchyg_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('lichkovo'))
async def lichkovo_cmd(callback_query: CallbackQuery):
    global city
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Лычково (Новомосковский р-н) *👨🏾‍🌾  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = lichkovo_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('illarionovo'))
async def illarionovo_cmd(callback_query: CallbackQuery):
    global city
    city = 'ПГТ Илларионово 🌻'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *ПГТ Илларионово *🌻 . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = illarionovo_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('carichanka'))
async def carichanka_cmd(callback_query: CallbackQuery):
    global city
    city = 'ПГТ Царичанка 🏘'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *ПГТ Царичанка *🏘 . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = carichanka_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('golubovka'))
async def golubovka_cmd(callback_query: CallbackQuery):
    global city
    city = 'Голубовка(Новомосковский район)'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Голубовка(Новомосковский район)*  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = golubovka_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('gor_plav'))
async def gorplav_cmd(callback_query: CallbackQuery):
    global city
    city = 'Горишние Плавни ⛪️'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Горишние Плавни *⛪️ . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = gorplav_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('podgorodnoe'))
async def podgorodnoe_cmd(callback_query: CallbackQuery):
    global city
    city = 'Подгородное (Днепропетровская обл)🏘'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Подгородное (Днепропетровская обл)*🏘  . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = podgorodnoe_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('novomoskovsk'))
async def novomsk_cmd(callback_query: CallbackQuery):
    global city
    city = 'Новомосковск 🚌'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Новомосковск *🚌 . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = novomoskovsk_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('jitomir'))
async def jitomir_cmd(callback_query: CallbackQuery):
    global city
    city = 'Житомир 🌾'
    await bot.send_message(chat_id = callback_query.from_user.id,
                    text='Вы выбрали город *Житомир*🌾 . Какой товар интересует?',
                    parse_mode='markdown',
                    reply_markup = jitomir_kb)

#////////////////////////////////////////////////////////////////POSITIONS NOV MAJ

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_novmaj'))
async def pesok10nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'Песок❄️0.1г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    try:
        await bot.send_message(chat_id=callback_query.from_user.id,
                           text=PES0_1,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    except:
        await bot.send_message(chat_id=callback_query.from_user.id,
                                text='Сначала выберите город!')

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_novmaj'))
async def pesok15nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/6qS0wXg2/photo-2021-02-08-22-35-21.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_novmaj'))
async def pesok25nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_novmaj'))
async def mef25nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'Меф МЯУ😻0.25г'
    price = 180
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_novmaj'))
async def mef50nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'Меф МЯУ😻0.5г'
    price = 350
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_novmaj'))
async def mef100nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_novmaj'))
async def alfa25nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    

@dp.callback_query_handler(lambda c: c.data.startswith('a1_novmaj'))
async def alfa100nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_novmaj'))
async def shish1nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 250
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1NM,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('sh2_novmaj'))
async def shish2nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новое Мажарово (Харьковская обл.) 🌳'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/TYX3GqKk/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
#/////////////////////////////////////////////////////////// VERHDNEPR

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_vd'))
async def pesok15vd(callback_query: CallbackQuery):
    global position, price,btcprice
    city = 'Верхнеднепровск 🆕'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)
    
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_vd'))
async def pesok25vd(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Верхнеднепровск 🆕'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)
    

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_vd'))
async def pesok50vd(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Верхнеднепровск 🆕'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes1_vd'))
async def pesok100vd(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Верхнеднепровск 🆕'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_vd'))
async def mef25vd(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Верхнеднепровск 🆕'
    position = 'Меф МЯУ😻0.25г'
    price = 153
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/ht03rZ99/photo-2023-03-30-10-42-29.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25VD,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_vd'))
async def mef50vd(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Верхнеднепровск 🆕'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5VD,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_vd'))
async def mef100vd(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Верхнеднепровск 🆕'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=vdtitova_kb)

#//////////////////////////////////////////////////////////////SINELNIKOVO

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_sin'))
async def rabota1sin(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Синельниково 🌾'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=novmajcentr_kb)
    
#/////////////////////////////////////////////////////////////////PAVLOGRAD

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_pg'))
async def alfa25pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Павлоград ⛏'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=pgpzto_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_pg'))
async def alfa50pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Павлоград ⛏'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=pgpzto_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_pg'))
async def alfa10pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Павлоград ⛏'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=pgpzto_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_pg'))
async def pesok15pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Павлоград ⛏'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=pgpzto_kb)
    
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_pg'))
async def pesok25pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Павлоград ⛏'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=pgpzto_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_pg'))
async def rabota1pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Павлоград ⛏'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=pgcentr_kb)

#///////////////////////////////////////////////////////////////KAMENSKOE

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_kam'))
async def pesok15kam(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Каменско́е (Днепродзержинск) 🏭'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=kamcher_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_kam'))
async def pesok50kam(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Каменско́е (Днепродзержинск) 🏭'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=kamcher_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_kam'))
async def pesok25kam(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Каменско́е (Днепродзержинск) 🏭'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25KAM,
                           parse_mode='markdown',
                           reply_markup=kamcher_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_kam'))
async def rabota1pg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Каменско́е (Днепродзержинск) 🏭'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=pgcentr_kb)

#////////////////////////////////////////////////////////////////////////////DNEPR

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_dnepr'))
async def alfa25dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=dnepra025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_dnepr'))
async def alfa50dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=dnepra05_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_dnepr'))
async def alfa100dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=dnepra1_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_dnepr'))
async def pesok15dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=dneprpes015_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_dnepr'))
async def pesok50dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=dneprpes05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_dnepr'))
async def pesok25dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=dneprpes025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_dnepr'))
async def mef25dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'Меф МЯУ😻0.25г'
    price = 153
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25VD,
                           parse_mode='markdown',
                           reply_markup=dneprmef025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_dnepr'))
async def mef50dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'Меф МЯУ😻0.5г'
    price = 320
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5DNEPR,
                           parse_mode='markdown',
                           reply_markup=dneprmef05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_dnepr'))
async def shish1dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=dneprshish1_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('sh2_dnepr'))
async def shish2dnepr(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Днепр 🏙 '
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=dneprshish2_kb)

#/////////////////////////////////////////////////////////////////////KREMENCHUG


@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_krem'))
async def pesok15krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15KAM,
                           parse_mode='markdown',
                           reply_markup=krempes15_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_krem'))
async def pesok50krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5CAR,
                           parse_mode='markdown',
                           reply_markup=krempes50_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_krem'))
async def pesok25krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25KAM,
                           parse_mode='markdown',
                           reply_markup=krempes25_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_krem'))
async def alfa25krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=krema025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_krem'))
async def alfa50krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=krema05_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_krem'))
async def alfa100krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=krema1_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_krem'))
async def mef50krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5VD,
                           parse_mode='markdown',
                           reply_markup=kremmef05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_krem'))
async def shish1krem(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Кременчуг 🌉'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/TYX3GqKk/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=kremsh1_kb)
    
#/////////////////////////////////////////////////////////////////////////////////////LICHKOVO

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_lich'))
async def alfa25lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=licha025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_lich'))
async def alfa50lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=licha05_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_lich'))
async def alfa100lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=licha1_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_lich'))
async def pesok15lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=lichpes015_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_lich'))
async def pesok25lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/6qS0wXg2/photo-2021-02-08-22-35-21.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=lichpes025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_lich'))
async def mef25lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'Меф МЯУ😻0.25г'
    price = 153
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25VD,
                           parse_mode='markdown',
                           reply_markup=lichmef025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_lich'))
async def mef50lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5VD,
                           parse_mode='markdown',
                           reply_markup=lichmef05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_lich'))
async def mef100lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=lichmef1_kb)


@dp.callback_query_handler(lambda c: c.data.startswith('sh1_lich'))
async def shish1lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 250
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1NM,
                           parse_mode='markdown',
                           reply_markup=lichshish1_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_lich'))
async def shish2lich(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Лычково (Новомосковский р-н) 👨🏾‍🌾'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/TYX3GqKk/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=lichshish2_kb)

#/////////////////////////////////////////////////////////////////////CARICHANKA

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_car'))
async def pesok15car(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Царичанка 🏘'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15KAM,
                           parse_mode='markdown',
                           reply_markup=carpes015_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_car'))
async def pesok25car(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Царичанка 🏘'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25KAM,
                           parse_mode='markdown',
                           reply_markup=carpes025_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_car'))
async def pesok50car(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Царичанка 🏘'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5CAR,
                           parse_mode='markdown',
                           reply_markup=carpes05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_car'))
async def pesok100car(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Царичанка 🏘'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=carpes1_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_car'))
async def rabota1car(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Царичанка 🏘'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=carrab1_kb)
    
#//////////////////////////////////////////////////////////////////////////////ILLARIONOVO

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_ila'))
async def pesok15illa(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Илларионово 🌻'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=illapes015_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_ila'))
async def pesok50illa(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Илларионово 🌻'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=illapes05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_ila'))
async def pesok25illa(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Илларионово 🌻'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=illapes025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_ila'))
async def mef50illa(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'ПГТ Илларионово 🌻'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5VD,
                           parse_mode='markdown',
                           reply_markup=illamef05_kb)

#////////////////////////////////////////////////////////////////////PERESHEPINO


@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_per'))
async def mef25per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Меф МЯУ😻0.25г'
    price = 153
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25VD,
                           parse_mode='markdown',
                           reply_markup=permef025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_per'))
async def mef50per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5VD,
                           parse_mode='markdown',
                           reply_markup=permef05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_per'))
async def mef100per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_per'))
async def alfa25per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_per'))
async def alfa50per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_per'))
async def alfa100per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_per'))
async def pesok10per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Песок❄️0.15г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_per'))
async def pesok15per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_per'))
async def pesok25per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=perpes025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_per'))
async def pesok50per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=perpes05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_per'))
async def pesok100per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=perpes1_kb)

    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_per'))
async def shish1per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_per'))
async def shish2per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=pershish2_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_per'))
async def rabota1per(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Перещепино 🌳'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=perrab1_kb)

#///////////////////////////////////////////////////////////////////////////////////GOLUBOVKA


@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_gol'))
async def mef25gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Меф МЯУ😻0.25г'
    price = 153
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/ht03rZ99/photo-2023-03-30-10-42-29.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25VD,
                           parse_mode='markdown',
                           reply_markup=golmef025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_gol'))
async def mef50gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_gol'))
async def mef100gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_gol'))
async def alfa25gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_gol'))
async def alfa50gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_gol'))
async def alfa100gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_gol'))
async def pesok10gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Песок❄️0.1г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_gol'))
async def pesok15gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_gol'))
async def pesok25gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_gol'))
async def pesok50gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_gol'))
async def pesok100gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_gol'))
async def shish1gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_gol'))
async def shish2gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=golshish2_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_gol'))
async def rabota1gol(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Голубовка(Новомосковский район)'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

#////////////////////////////////////////////////////////////////////GORISHNI PLAVNI


@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_gp'))
async def mef25gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Меф МЯУ😻0.25г'
    price = 180
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_gp'))
async def mef50gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5VD,
                           parse_mode='markdown',
                           reply_markup=gpmef05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_gp'))
async def mef100gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_gp'))
async def alfa25gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_gp'))
async def alfa50gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=gpa05_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_gp'))
async def alfa100gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_gp'))
async def pesok10gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Песок❄️0.1г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_gp'))
async def pesok15gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_gp'))
async def pesok25gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25KAM,
                           parse_mode='markdown',
                           reply_markup=gppes025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_gp'))
async def pesok50gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_gp'))
async def pesok100gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_gp'))
async def shish1gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_gp'))
async def shish2gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_gp'))
async def rabota1gp(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Горишние Плавни ⛪️'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 2000
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA2,
                           parse_mode='markdown',
                           reply_markup=gprab2_kb)

#/////////////////////////////////////////////////////////////////////////////////////////////PODGORODNOE


@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_podg'))
async def mef25podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Меф МЯУ😻0.25г'
    price = 180
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_podg'))
async def mef50podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_podg'))
async def mef100podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_podg'))
async def alfa25podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/tJTxwF61/photo-2020-07-08-19-09-09.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=podga025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_podg'))
async def alfa50podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/tJTxwF61/photo-2020-07-08-19-09-09.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=podga05_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_podg'))
async def alfa100podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/tJTxwF61/photo-2020-07-08-19-09-09.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=podga1_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_podg'))
async def pesok10podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Песок❄️0.1г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_podg'))
async def pesok15podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15KAM,
                           parse_mode='markdown',
                           reply_markup=podgpes015_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_podg'))
async def pesok25podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25KAM,
                           parse_mode='markdown',
                           reply_markup=podgpes025_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_podg'))
async def pesok50podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=podgpes05_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_podg'))
async def pesok100podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=podgpes1_kb)

    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_podg'))
async def shish1podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=podgshish1_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_podg'))
async def shish2podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_podg'))
async def rabota1podg(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Подгородное (Днепропетровская обл)🏘'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=podgrab1_kb)

#/////////////////////////////////////////////////////////////////////////////////NOVOMOSKOVSK


@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_nm'))
async def mef25nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Меф МЯУ😻0.25г'
    price = 180
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_nm'))
async def mef50nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_nm'))
async def mef100nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_nm'))
async def alfa25nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_nm'))
async def alfa50nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_nm'))
async def alfa100nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_nm'))
async def pesok10nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Песок❄️0.1г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_nm'))
async def pesok15nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15KAM,
                           parse_mode='markdown',
                           reply_markup=nmpes015_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_nm'))
async def pesok25nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_nm'))
async def pesok50nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_nm'))
async def pesok100nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_nm'))
async def shish1nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_nm'))
async def shish2nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota1_nm'))
async def rabota1nm(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Новомосковск 🚌'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA1,
                           parse_mode='markdown',
                           reply_markup=nmrab1_kb)

#////////////////////////////////////////////////////////////////////////////////////////////JITOMIR


@dp.callback_query_handler(lambda c: c.data.startswith('m0.25_jt'))
async def mef25jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Меф МЯУ😻0.25г'
    price = 180
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m0.5_jt'))
async def mef50jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Меф МЯУ😻0.5г'
    price = 315
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('m1_jt'))
async def mef100jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Меф МЯУ😻1г'
    price = 540
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/nrtRg7jj/photo-2022-09-16-16-19-49.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= M1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a0.25_jt'))
async def alfa25jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'А(ф-фат)⚡️0.25г'
    price = 150
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('a0.5_jt'))
async def alfa50jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'А(ф-фат)⚡️0.5г'
    price = 230
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('a1_jt'))
async def alfa100jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'А(ф-фат)⚡️1г'
    price = 400
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/LXJCmHGT/photo-2021-02-08-21-43-28.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= A1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.1_jt'))
async def pesok10jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Песок❄️0.1г'
    price = 200
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/kgFL5ZbL/photo-2020-11-17-21-09-56.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.15_jt'))
async def pesok15jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Песок❄️0.15г'
    price = 356
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_15,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('pes0.25_jt'))
async def pesok25jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Песок❄️0.25г'
    price = 570
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_25,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes0.5_jt'))
async def pesok50jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Песок❄️0.5г'
    price = 950
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES0_5,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('pes1_jt'))
async def pesok100jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'Песок❄️1 г'
    price = 1500
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/cJ9kqKkC/photo-2023-04-01-14-40-19.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= PES1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

    
@dp.callback_query_handler(lambda c: c.data.startswith('sh1_jt'))
async def shish1jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'ШШ Marmelad Kush🥬🆕1г'
    price = 280
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/pdXc1QZ3/photo-2023-04-01-15-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH1,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('sh2_jt'))
async def shish2jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'ШШ Marmelad Kush🥬2 г'
    price = 520
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/zBXMLSwy/photo-2021-07-10-12-14-15.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= SH2,
                           parse_mode='markdown',
                           reply_markup=shablon_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('rabota2_jt'))
async def rabota2jt(callback_query: CallbackQuery):
    global position, price, btcprice, city, number
    city = 'Житомир 🌾'
    position = 'РАБОТА КУРЬЕРОМ 👲🏾'
    price = 2000
    btcprice = convert_to_btc(price)
    number +=1
    await bot.send_photo(chat_id=callback_query.from_user.id,
                         photo='https://i.postimg.cc/y8Kb0CS1/photo-2020-12-16-19-18-47.jpg')
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= RABOTA2,
                           parse_mode='markdown',
                           reply_markup=jtrab2_kb)


#////////////////////////////////////////////////////////////////////////////////////////////////ZAKAZ
def createzakaz1(district):
    global city, position, price
    createzakaz = f'''🎁Ваш заказ № {number}: 
    🏢Город: {city}. 
    🏢Район: {district}. 
    💊Товар: {position}. 
    💵Цена: {price}.

    *‼️⏱ Время бронирования товара - 30 мин (кроме оплаты Bitcoin). По источению времени заказ будет отменен, а прием и проверка оплаты ботом за указанный заказ - невозможна. Если не успеваете - нажмите "Просмотреть статус", а затем "Продлить время бронирования". 

    ‼️Маскимальное количество броней в день - 5. БОЛЬШЕ 5 ЗАКАЗОВ ЗА СУТКИ БЕЗ ОПЛАТЫ ТОВАРА - БАН!

    ℹ️Если вы оплатили товар, а заказ отменился - свяжитесь с @HELPER_MARM
    для проверки платежа и выдачи заказа в ручном режиме*  

    Выберите удобный метод платы:'''
    return createzakaz

def paybtc1(district):
    global city, position, price, number
    paybtc = f'''🎁Ваш заказ № {number}:
    🏢Город: {city}. 
    🏢Район: {district}. 
    💊Товар: {position}. 
    💵Цена: {price}.
    Чтобы отследить заказ на сайте, оставить отзыв или написать запрос в службу поддержки, воспользуйтесь своим /pin и номером заказа 238551.


    ℹ️Выбран метод оплаты Bitcoin.
    💸Для получения товара, оплатите на кошелек Реки давай сумму {round(btcprice, 6)} Btc.
    После оплаты нажмит кнопку СТАТУС или введи команду /status

    📜‼️Обязательно прочтите правила магазина MARMELAD SHOP (https://telegra.ph/PRAVILA-DLYA-KLIENTOV-MARMELAD-SHOP-04-18) перед покупкой!‼️'''

    return paybtc

def paycard1(district):
    global city, position, price, pricepercent, number
    paycard = f'''🎁Ваш заказ № {number}:
    🏢Город: {city}. 
    🏢Район: {district}. 
    💊Товар: {position}. 
    💵Цена: {int(pricepercent)}.
    Чтобы отследить заказ на сайте, оставить отзыв или написать запрос в службу поддержки, воспользуйтесь своим /pin и номером заказа {number}.


    💳 Выбран метод оплаты на банковкую карту

    ❗️⏱На оплату дается 30 минут
    Для получения товара, оплатите на карту  Давай уже реквизиты  сумму {int(pricepercent)} грн.
    ℹ️Проверка статуса оплаты в боте: @godsupbot
    ℹ️Код заявки: `WD-{code}`


    Сумма оплаты должна быть ровно {int(pricepercent)} грн. поэтому при оплате заказа этим способом используйте онлайн-банкинг (например Приват24) или терминалы самообслуживания, которые зачисляют сдачу на ваш счет (например терминалы Приватбанка)
    Статус оплаты можно узнать в боте getBTC @godsupbot , нажав "У меня проблема" и отправив боту код заявки  WD-{code}  (бот не выдаст фото пока у заявки не будет статус "Оплачена")
    ❗️ПРОЧТИТЕ ЧТОБ НЕ ПРОЕБАТЬ ДЕНЬГИ И КЛАД❗️: Оплачивайте одним платежом! Сохраняйте чек или скриншот с онлайн-банкинга! Не оплачивайте заявку по истечению срока бронирования заказа! Не оплачивайте больше или меньше, чем указано! Не используйте терминалы IBOX, City24 и подобные при оплате данным способом! При несоблюдении вышесказанного вы можете потерять свои деньги! После оплаты на решение вопроса по проблемному платежу дается 48 часов, после этого информация о заявке безвозвратно удаляется  из системы GetBTC!
    Время зачисления платежа 5-30 минут (зависит от совместимости банков, скорости интернета и погодных условий. Терминалы ПриватБанка иногда задерживают платежи на 20-30 мин). После оплаты подождите немного, после чего нажмите 👉🏽 /status для проверки статуса Вашего платежа.
    ℹ️ В случае если что-то пошло не так и :
    - вы оплатили неточную сумму
    - вы оплатили несколькими платежами
    - вы оплатили после отмены заказа
    - вы оплатили, но адрес не пришел и заказ отменился
    перейдите в бот @godsupbot , отправьте ему номер заявки  WD-{code}  и следуйте подсказкам в боте, а после подтверждения - к @HELPER\_MARM
    📜‼️Обязательно прочтите правила магазина MARMELAD SHOP (https://telegra.ph/PRAVILA-DLYA-KLIENTOV-MARMELAD-SHOP-04-18) перед покупкой!‼️
    '''
    return paycard

def payglobal1(district):
    global city, position, price, number
    paycard = f'''🎁Ваш заказ № {number}:
    🏢Город: {city}. 
    🏢Район: {district}. 
    💊Товар: {position}. 
    💵Цена: {price}.
    Чтобы отследить заказ на сайте, оставить отзыв или написать запрос в службу поддержки, воспользуйтесь своим /pin и номером заказа {number}.


    💸Выбран метод оплаты Global24.pro. Для получения товара, оплатите на кошелек ГДЕ КОШ? сумму 375 грн..
    Кошелек ДАВАЙ КОШ Ваш только на время бронирования, не оплачивайте на него по истечению срока бронирования заказа!

    Для оплаты с банковской карты 💳  перейдите по ссылке  https://global24.pro/replenishbycard (регистрация не нужна)
    Приложение Global24 для Android https://play.google.com/store/apps/details?id=ua.com.global24.global24
    Приложение Global24 для iOS https://itunes.apple.com/ru/app/global24/id1458873410
    ℹ️ Если не работает оплата с карты -  можете попробовать в приложении использовать пополнение кошелька с Vodafone на Globalmoney 
    После оплаты, дождитесь обработки платежа, адрес прийдет автоматически в течении 10 мин. 

    ℹ️Не паникуйте, если адрес не выдало моментально. Обычно всё происходит быстро, но в редких случаях по техническим причинам проверка оплаты занимает до 30 мин.
    ℹ️Если ничего не получилось - свяжитесь с @HELPER_MARM для проверки платежа и выдачи заказа в ручном режиме.

    📜‼️Обязательно прочтите правила магазина MARMELAD SHOP (https://telegra.ph/PRAVILA-DLYA-KLIENTOV-MARMELAD-SHOP-04-18) перед покупкой!‼️'''
    return paycard

def convert_to_btc(price):
    global btc_price
    # API ключ и секретный ключ Binance
    api_key = 'ZGM4xtq8CRY3e3rHRMaiFYcFtHfTNWdUF8q6NH0rJAFS8eGHkixLKHAcMosr9abn'
    secret_key = 'zHum7JppFH0sB3DzVSDNjZ6P1QVj8TJrAcvPb8ZDIgksRHogGqKDwlNzWgCI0Mcp'

    # URL для получения текущего курса обмена
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUAH'

    # Запрос к API Binance
    response = requests.get(url)

    # Парсинг JSON-ответа
    data = json.loads(response.text)

    # Получение текущего курса обмена

    btc_price = float(data['price'])

    # Конвертация цены из гривен в биткоины
    btc_amount = price / btc_price

    return btc_amount

payments_kb = InlineKeyboardMarkup(row_width=1)

@dp.callback_query_handler(lambda c: c.data.startswith('zakaz'))
async def zakaz(callback_query: CallbackQuery):
    global district, pricepercent
    district = callback_query.data.split('|')[1]
    pricepercent = int(price) * 1.15
    payments_kb = InlineKeyboardMarkup(row_width=1)
    pay_kb = payments_kb.add(InlineKeyboardButton(f'На карту💳📟.К оплате: {int(pricepercent)}', callback_data='cardprice'),
                             InlineKeyboardButton(f'Global24.pro💳.К оплате: {price}', callback_data='clearprice'),
                             InlineKeyboardButton(f'Bitcoin 💰. К оплате: {round(btcprice, 6)}', callback_data='btcprice'),
                             InlineKeyboardButton('Отменить заказ', callback_data='cancelpay'))
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= createzakaz1(district),
                           parse_mode= 'markdown',
                           reply_markup=pay_kb)

@dp.callback_query_handler(lambda c: c.data == 'btcprice')
async def btcpayment(callback_query: CallbackQuery):
    global district, pricepercent
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= paybtc1(district),
                           parse_mode= 'markdown',
                           reply_markup= afterpay_kb
                           )
    
@dp.callback_query_handler(lambda c: c.data == 'cardprice')
async def cardpayment(callback_query: CallbackQuery):
    global district
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= paycard1(district),
                           reply_markup= afterpay_kb,
                           parse_mode='markdown',
                           )
    
@dp.callback_query_handler(lambda c: c.data == 'clearprice')
async def globalpayment(callback_query: CallbackQuery):
    global district, price
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text= payglobal1(district),
                           reply_markup= afterpay_kb
                           )

@dp.callback_query_handler(lambda c: c.data == 'cancelpay1')
async def cancelpayment(callback_query: CallbackQuery):
    global number
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f'Заказ № {number} будет отменен. Ты уверен?!',
                           reply_markup=cancelpay1_kb)


@dp.callback_query_handler(lambda c: c.data == 'cancelpay2')
async def cancelpayment(callback_query: CallbackQuery):
    global number, username
    user = callback_query.from_user
    username = user.first_name
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f'Ваш заказ № {number} успешно отменен!')
    await bot.send_message(chat_id=callback_query.from_user.id,
                            text='Боты ☯️ сайты ⚡️odium.co')
    await bot.send_message(chat_id=callback_query.from_user.id,
                            text =f'*{username}* {START_MES}',
                            reply_markup = start_kb,
                            parse_mode='markdown')

def statusmsg():
    global number, city,district,position,price        
    status = f'''ℹ️*Оплата ожидается*
    Если вы оплатили свой заказ и с момента оплаты прошло не более 20 минут, не стоит волноваться. 
    🔸*При оплате с помощью Bitcoin*| возможны задержки до нескольких часов, в зависимости от комиссии и загруженности сети.

    🎁Ваш заказ № {number}:
        🏢Город: {city}. 
        🏢Район: {district}. 
        💊Товар: {position}. 
        💵Цена: {price}.
        Чтобы отследить заказ на сайте, оставить отзыв или написать запрос в службу поддержки, воспользуйтесь своим /pin и номером заказа 240057.'''
    return status

@dp.callback_query_handler(lambda c: c.data == 'checkstatus')
async def statuscheck(callback_query: CallbackQuery):
    global number,city,district,position,price
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=statusmsg(),
                           reply_markup=checkstatus_kb,
                           parse_mode='markdown')
    
@dp.callback_query_handler(lambda c: c.data == 'help')
async def help_cmd(callback_query: CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=HELP,
                           parse_mode='markdown')
                           

@dp.callback_query_handler(lambda c: c.data == 'longtime')
async def longertime(callback_query: CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text='Сейчас нельзя это сделать')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)