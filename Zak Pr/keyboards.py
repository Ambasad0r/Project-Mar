from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




start_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard= [    
    [InlineKeyboardButton('Верхнеднепровск 🆕', callback_data='verhdnepr'),InlineKeyboardButton('Новое Мажарово (Харьковская обл.) 🌳', callback_data='nov_maj')],
    [InlineKeyboardButton('Синельниково 🌾', callback_data='sinelnikovo'),InlineKeyboardButton('Павлоград⛏', callback_data='pavlograd')],
    [InlineKeyboardButton('Каменско́е (Днепродзержинск) 🏭', callback_data='kamenskoe'),InlineKeyboardButton('Днепр 🏙', callback_data='dnepr')],
    [InlineKeyboardButton('Перещепино 🌳', callback_data='pereshepino'),InlineKeyboardButton('ПГТ Царичанка 🏘', callback_data='carichanka')],
    [InlineKeyboardButton('Кременчуг 🌉', callback_data='kremenchug'),InlineKeyboardButton('ПГТ Илларионово 🌻', callback_data='illarionovo')],
    [InlineKeyboardButton('Лычково (Новомосковский р-н) 👨🏾‍🌾', callback_data='lichkovo'),InlineKeyboardButton('Голубовка(Новомосковский район)', callback_data='golubovka')],
    [InlineKeyboardButton('Житомир 🌾', callback_data='jitomir'), InlineKeyboardButton('Горишние Плавни ⛪️', callback_data='gor_plav')],
    [InlineKeyboardButton('Подгородное (Днепропетровская обл) 🏘', callback_data='podgorodnoe'),InlineKeyboardButton('Новомосковск 🚌', callback_data='novomoskovsk')]
])

nov_maj_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️0.1г 200грн.', callback_data= 'pes0.1_novmaj')],
    [InlineKeyboardButton('А(ф-фат)⚡️0.25г 150грн.', callback_data = 'a0.25_novmaj')],
    [InlineKeyboardButton('А(ф-фат)⚡️1г 400грн.', callback_data = 'a1_novmaj')],
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_novmaj')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.',callback_data = 'pes0.25_novmaj')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕1г 250грн.',callback_data = 'sh1_novmaj')],
    [InlineKeyboardButton('Меф МЯУ😻1г 540грн.',callback_data = 'm1_novmaj')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 350грн.',callback_data = 'm0.5_novmaj')],
    [InlineKeyboardButton('Меф МЯУ😻0.25г 180грн.',callback_data = 'm0.25_novmaj')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕2г 520грн.',callback_data = 'sh2_novmaj')]
])

verhdnepr_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_vd')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_vd')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.' ,callback_data = 'pes0.5_vd')],
    [InlineKeyboardButton('Песок❄️1г 1500грн.' ,callback_data = 'pes1_vd')],
    [InlineKeyboardButton('Меф МЯУ😻0.25г 153грн.',callback_data = 'm0.25_vd')],
    [InlineKeyboardButton('Меф МЯУ😻1 г 540грн.',callback_data = 'm1_vd')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 315грн.',callback_data = 'm0.5_vd')]

])

sinelnik_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_sin')]
])

pavlograd_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('А(ф-фат)⚡️0.25г 150грн.', callback_data = 'a0.25_pg')],
    [InlineKeyboardButton('А(ф-фат)⚡️1 г 400грн.', callback_data = 'a1_pg')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_pg')],
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_pg')],
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_pg')]
])

kamenskoe_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_kam')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.' ,callback_data = 'pes0.5_kam')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_kam')],
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_kam')]
])

dnepr_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('А(ф-фат)⚡️0.25г 150грн.', callback_data = 'a0.25_dnepr')],
    [InlineKeyboardButton('А(ф-фат)⚡️0.5г 230грн.', callback_data = 'a0.5_dnepr')],
    [InlineKeyboardButton('А(ф-фат)⚡️1 г 400грн.', callback_data = 'a1_dnepr')],
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_dnepr')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.',callback_data = 'pes0.25_dnepr')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.',callback_data = 'pes0.5_dnepr')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕1г 280грн.',callback_data = 'sh1_dnepr')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕2 г 520грн.',callback_data = 'sh2_dnepr')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 320грн.',callback_data = 'm0.5_dnepr')],
    [InlineKeyboardButton('Меф МЯУ😻0.25г 153грн.',callback_data = 'm0.25_dnepr')],
])

pereshepino_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️1 г 1500грн.' ,callback_data = 'pes1_per')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.',callback_data = 'pes0.5_per')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.',callback_data = 'pes0.25_per')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 315грн.',callback_data = 'm0.5_per')],
    [InlineKeyboardButton('Меф МЯУ😻0.25г 153грн.',callback_data = 'm0.25_per')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕2 г 520грн.',callback_data = 'sh2_per')],
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_per')]
])

kremenchyg_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_krem')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.',callback_data = 'pes0.25_krem')],
    [InlineKeyboardButton('А(ф-фат)⚡️1 г 400грн.', callback_data = 'a1_krem')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.',callback_data = 'pes0.5_krem')],
    [InlineKeyboardButton('А(ф-фат)⚡️0.25г 150грн.', callback_data = 'a0.25_krem')],
    [InlineKeyboardButton('А(ф-фат)⚡️0.5г 230грн.', callback_data = 'a0.5_krem')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 315грн.',callback_data = 'm0.5_krem')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕1 г 280грн.',callback_data = 'sh1_krem')],
])

lichkovo_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('А(ф-фат)⚡️0.25г 150грн.', callback_data = 'a0.25_lich')],
    [InlineKeyboardButton('А(ф-фат)⚡️0.5г 230грн.', callback_data = 'a0.5_lich')],
    [InlineKeyboardButton('А(ф-фат)⚡️1 г 400грн.', callback_data = 'a1_lich')],
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_lich')],
    [InlineKeyboardButton('Меф МЯУ😻1 г 540грн.',callback_data = 'm1_lich')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_lich')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕2 г 520грн.',callback_data = 'sh2_lich')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕1 г 250грн.',callback_data = 'sh1_lich')],
    [InlineKeyboardButton('Меф МЯУ😻0.25г 153грн.',callback_data = 'm0.25_lich')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 315грн.',callback_data = 'm0.5_lich')]
])

illarionovo_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_ila')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_ila')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.' ,callback_data = 'pes0.5_ila')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 315грн.',callback_data = 'm0.5_ila')]
])

carichanka_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️1г 1500грн.' ,callback_data = 'pes1_car')],
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_car')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_car')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.' ,callback_data = 'pes0.5_car')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕2 г 480грн.',callback_data = 'sh2_car')],
    [InlineKeyboardButton(' КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_car')]
])

golubovka_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Меф МЯУ😻0.25г 153грн.',callback_data = 'm0.25_gol')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕2 г 520грн.',callback_data = 'sh2_gol')],
    
])

gorplav_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('А(ф-фат)⚡️0.5г 230грн.', callback_data = 'a0.5_gp')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_gp')],
    [InlineKeyboardButton('Меф МЯУ😻0.5г 315грн.',callback_data = 'm0.5_gp')],
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 2000грн.', callback_data= 'rabota1_gp')]

])

podgorodnoe_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('А(ф-фат)⚡️0.25г 150грн.', callback_data = 'a0.25_podg')],
    [InlineKeyboardButton('А(ф-фат)⚡️0.5г 230грн.', callback_data = 'a0.5_podg')],
    [InlineKeyboardButton('А(ф-фат)⚡️1 г 400грн.', callback_data = 'a1_podg')],
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_podg')],
    [InlineKeyboardButton('Песок❄️0.25г 570грн.' ,callback_data = 'pes0.25_podg')],
    [InlineKeyboardButton('Песок❄️0.5г 950грн.' ,callback_data = 'pes0.5_podg')],
    [InlineKeyboardButton('Песок❄️1 г 1500грн.' ,callback_data = 'pes1_podg')],
    [InlineKeyboardButton('ШШ Marmelad Kush🥬🆕1 г 250грн.',callback_data = 'sh1_podg')],
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_podg')],

])

novomoskovsk_kb= InlineKeyboardMarkup(row_width=2, inline_keyboard= [
    [InlineKeyboardButton('Песок❄️0.15г 356грн.' ,callback_data = 'pes0.15_nm')],
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 1500грн.', callback_data= 'rabota1_nm')]

])

jitomir_kb = InlineKeyboardMarkup(row_width=2 , inline_keyboard=[
    [InlineKeyboardButton('РАБОТА КУРЬЕРОМ 👲🏾 2000грн.', callback_data= 'rabota2_jt')]
])

#//////////////////////////////////////////////////////NOV MAJ

novmajcentr_kb = InlineKeyboardMarkup(row_width = 2, inline_keyboard = [
    [InlineKeyboardButton('Центральная 🌆', callback_data='zakaz|Центральная 🌆')]
])

#////////////////////////////////////////////////////////VERHNEDNIPROVSK

vdtitova_kb = InlineKeyboardMarkup(row_width=2)
vdtitova_kb.add(InlineKeyboardButton('Титова🌇', callback_data= 'zakaz|Титова🌇'))

#////////////////////////////////////////////////////////////PAVLOGRAD


pgpzto_kb = InlineKeyboardMarkup(row_width=2)
pgpzto_kb.add(InlineKeyboardButton('ПЗТО 🌳', callback_data = 'zakaz|ПЗТО 🌳'))

pgcentr_kb = InlineKeyboardMarkup(row_width=2)
pgcentr_kb.add(InlineKeyboardButton('Центр🌆', callback_data='zakaz|Центр🌆'))

#///////////////////////////////////////////////////////////KAMENSKOE

kamcher_kb = InlineKeyboardMarkup(row_width=2)
kamcher_kb.add(InlineKeyboardButton('Черёмушки🌲', callback_data='zakaz|Черёмушки🌲'))

#/////////////////////////////////////////////////////////DNEPR KB



dnepra025_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Рабочая🚃', callback_data= 'zakaz|Рабочая🚃'),InlineKeyboardButton('Петровского🏭', callback_data= 'zakaz|Петровского🏭')],
    [InlineKeyboardButton('Левобережный-3🗽',callback_data='zakaz|Левобережный-3🗽'),InlineKeyboardButton('Солнечный🛕', callback_data='zakaz|Солнечный🛕')],
    [InlineKeyboardButton('Шинная(ТРЦ Дафи)🏬', callback_data='zakaz|Шинная(ТРЦ Дафи)🏬'),InlineKeyboardButton('Тополь-1🏤', callback_data= 'zakaz|Тополь-1🏤')],
    [InlineKeyboardButton('Калиновая🍒', callback_data='zakaz|Калиновая🍒'),InlineKeyboardButton('Гагарина (ДНУ)👩🏿‍🚀', callback_data='zakaz|Гагарина (ДНУ)👩🏿‍🚀')],
    [InlineKeyboardButton('ул.Каруны🚙', callback_data='zakaz|ул.Каруны🚙'),InlineKeyboardButton('Кирова верх🏢', callback_data='zakaz|Кирова верх🏢')],
    [InlineKeyboardButton('Маршала Малиновского💂🏾', callback_data='zakaz|Маршала Малиновского💂🏾')]
]) 

dnepra05_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Петровского🏭', callback_data='zakaz|Петровского🏭'),InlineKeyboardButton('Левобережный-3🗽',callback_data='zakaz|Левобережный-3🗽')],
    [InlineKeyboardButton('Солнечный🛕', callback_data='zakaz|Солнечный🛕'),InlineKeyboardButton('Калиновая🍒', callback_data='zakaz|Калиновая🍒')],
    [InlineKeyboardButton('ул.Каруны🚙', callback_data='zakaz|ул.Каруны🚙'),InlineKeyboardButton('Северный🌫', callback_data='zakaz|Северный🌫')],
    [InlineKeyboardButton('Кирова верх🏢', callback_data='zakaz|Кирова верх🏢'),InlineKeyboardButton('Маршала Малиновского💂🏾', callback_data='zakaz|Маршала Малиновского💂🏾')]
])

dnepra1_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Петровского🏭', callback_data='zakaz|Петровского🏭'),InlineKeyboardButton('Маршала Малиновского💂🏾', callback_data='zakaz|Маршала Малиновского💂🏾')],
])

dneprpes015_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Рабочая🚃', callback_data= 'zakaz|Рабочая🚃'),InlineKeyboardButton('Петровского🏭', callback_data= 'zakaz|Петровского🏭')],
    [InlineKeyboardButton('Победы (р-н кольца🍟)', callback_data='zakaz|Победы (р-н кольца🍟)'),InlineKeyboardButton('Метеор(Зеленый Гай)🌳', callback_data='zakaz|Метеор(Зеленый Гай)🌳')],
    [InlineKeyboardButton('Шинная(ТРЦ Дафи)🏬', callback_data='zakaz|Шинная(ТРЦ Дафи)🏬'),InlineKeyboardButton('ж/м Сокол🦅', callback_data='zakaz|ж/м Сокол🦅')],
    [InlineKeyboardButton('Криворожская(ЮМЗ)🚀', callback_data='zakaz|Криворожская(ЮМЗ)🚀'),InlineKeyboardButton('Гагарина(ДИИТ)👨‍🚀', callback_data='zakaz|Гагарина (ДНУ)👩🏿‍🚀')],
    [InlineKeyboardButton('Титова🧱', callback_data='zakaz|Титова🧱'),InlineKeyboardButton('Игрень🍻', callback_data='zakaz|Игрень🍻')],
    [InlineKeyboardButton('Кирова верх🏢', callback_data='zakaz|Кирова верх🏢'),InlineKeyboardButton('Кирова низ🏢', callback_data='zakaz|Кирова низ🏢')],
    [InlineKeyboardButton('Левобережный-3🗽',callback_data='zakaz|Левобережный-3🗽'),InlineKeyboardButton('Маршала Малиновского💂🏾', callback_data='zakaz|Маршала Малиновского💂🏾')]
]) 

dneprpes025_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Кирова🏢', callback_data='zakaz|Кирова🏢'),InlineKeyboardButton('Рабочая🚃', callback_data= 'zakaz|Рабочая🚃')],
    [InlineKeyboardButton('Петровского🏭', callback_data= 'zakaz|Петровского🏭'),InlineKeyboardButton('Победы (р-н кольца)🍟', callback_data='zakaz|Победы (р-н кольца🍟)')],
    [InlineKeyboardButton('Метеор(Зеленый Гай)🌳', callback_data='zakaz|Метеор(Зеленый Гай)🌳'),InlineKeyboardButton('ТЦ "Нагорка"🎢', callback_data='zakaz|ТЦ "Нагорка"🎢')],
    [InlineKeyboardButton('Космическая(Лавина)🏂', callback_data='zakaz|Космическая(Лавина)🏂'),InlineKeyboardButton('Криворожская(ЮМЗ)🚀', callback_data='zakaz|Криворожская(ЮМЗ)🚀')],
    [InlineKeyboardButton('Титова🧱', callback_data='zakaz|Титова🧱'),InlineKeyboardButton('Кирова верх🏢', callback_data='zakaz|Кирова верх🏢')],
    [InlineKeyboardButton('Кирова низ🏢', callback_data='zakaz|Кирова низ🏢')],
]) 

dneprpes05_kb = InlineKeyboardMarkup(row_width=2)
dneprpes05_kb.add(InlineKeyboardButton('Победы (р-н кольца)🍟', callback_data='zakaz|Победы (р-н кольца🍟)'))

dneprmef05_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('ж/м Парус⛵️',callback_data='dneprpar_mef50'),InlineKeyboardButton('жм Западный🌄',callback_data='zakaz|жм Западный🌄')],
])

dneprmef025_kb = InlineKeyboardMarkup(row_width=2)
dneprmef025_kb.add(InlineKeyboardButton('Диевка🏡', callback_data='zakaz|Диевка🏡'))

dneprshish1_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Петровского🏭', callback_data= 'zakaz|Петровского🏭'),InlineKeyboardButton('Метеор(Зеленый Гай)🌳', callback_data='zakaz|Метеор(Зеленый Гай)🌳')],
    [InlineKeyboardButton('ж/м Сокол🦅', callback_data='zakaz|ж/м Сокол🦅')],
])

dneprshish2_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton('Левобережный-3🗽',callback_data='zakaz|Левобережный-3🗽')]
])
#/////////////////////////////////////////////////////////////////////////////KREMENCHUG

krempes15_kb = InlineKeyboardMarkup(row_width=2)
krempes15_kb.add(InlineKeyboardButton('Крюков🏖',callback_data='zakaz|Крюков🏖'))
krempes25_kb = InlineKeyboardMarkup(row_width=2)
krempes25_kb.add(InlineKeyboardButton('Крюков🏖',callback_data='zakaz|Крюков🏖'))
krempes50_kb = InlineKeyboardMarkup(row_width=2)
krempes50_kb.add(InlineKeyboardButton('Крюков🏖',callback_data='zakaz|Крюков🏖'))

krema1_kb = InlineKeyboardMarkup(row_width=2)
krema1_kb.add(InlineKeyboardButton('Карьер🧗🏾‍♂️',callback_data='zakaz|Карьер🧗🏾‍♂️'))
krema025_kb = InlineKeyboardMarkup(row_width=2)
krema025_kb.add(InlineKeyboardButton('Крюковский карьер👷‍♂️',callback_data='zakaz|Крюковский карьер👷‍♂️'))
krema05_kb = InlineKeyboardMarkup(row_width=2)
krema05_kb.add(InlineKeyboardButton('Крюковский карьер👷‍♂️',callback_data='zakaz|Крюковский карьер👷‍♂️'))

kremsh1_kb = InlineKeyboardMarkup()
kremsh1_kb.add(InlineKeyboardButton('Крюков🏖',callback_data='zakaz|Крюков🏖'),InlineKeyboardButton('Крюковский карьер👷‍♂️',callback_data='zakaz|Крюковский карьер👷‍♂️'))

kremmef05_kb = InlineKeyboardMarkup()
kremmef05_kb.add(InlineKeyboardButton('Арт Склады💂',callback_data='zakaz|Арт Склады💂'),InlineKeyboardButton('Крюковский карьер👷‍♂️',callback_data='zakaz|Крюковский карьер👷‍♂️'))

#///////////////////////////////////////////////////////LICHKOVO

licha025_kb = InlineKeyboardMarkup()
licha025_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

licha05_kb = InlineKeyboardMarkup()
licha05_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

licha1_kb = InlineKeyboardMarkup()
licha1_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichpes015_kb = InlineKeyboardMarkup()
lichpes015_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichpes025_kb = InlineKeyboardMarkup()
lichpes025_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichmef025_kb = InlineKeyboardMarkup()
lichmef025_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichmef05_kb = InlineKeyboardMarkup()
lichmef05_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichmef1_kb = InlineKeyboardMarkup()
lichmef1_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichshish1_kb = InlineKeyboardMarkup()
lichshish1_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

lichshish2_kb = InlineKeyboardMarkup()
lichshish2_kb.add(InlineKeyboardButton('Орель🚣🏾',callback_data='zakaz|Орель🚣🏾'))

#///////////////////////////////////////////////////////////////////////////////////CARICHANKA

carpes015_kb = InlineKeyboardMarkup()
carpes015_kb.add(InlineKeyboardButton('ул.Лесная🌳', callback_data='zakaz|ул.Лесная🌳'))

carpes025_kb = InlineKeyboardMarkup()
carpes025_kb.add(InlineKeyboardButton('ул.Лесная🌳', callback_data='zakaz|ул.Лесная🌳'))

carpes05_kb = InlineKeyboardMarkup()
carpes05_kb.add(InlineKeyboardButton('ул.Лесная🌳', callback_data='zakaz|ул.Лесная🌳'))

carpes1_kb = InlineKeyboardMarkup()
carpes1_kb.add(InlineKeyboardButton('Набережная🏖', callback_data='zakaz|Набережная🏖'))

carrab1_kb = InlineKeyboardMarkup()
carrab1_kb.add(InlineKeyboardButton('Автовокзал 🏪', callback_data='zakaz|Автовокзал 🏪'))

#///////////////////////////////////////////////////////////////////////////ILLARIONOVO

illapes015_kb = InlineKeyboardMarkup()
illapes015_kb.add(InlineKeyboardButton('Парк🌳', callback_data='zakaz|Парк🌳'))

illapes025_kb = InlineKeyboardMarkup()
illapes025_kb.add(InlineKeyboardButton('Парк🌳', callback_data='zakaz|Парк🌳'))

illapes05_kb = InlineKeyboardMarkup()
illapes05_kb.add(InlineKeyboardButton('Парк🌳', callback_data='zakaz|Парк🌳'))

illamef05_kb = InlineKeyboardMarkup()
illamef05_kb.add(InlineKeyboardButton('Парк🌳', callback_data='zakaz|Парк🌳'))



#/////////////////////////////////////////////////////////////////////////////PEREWEPINO

perpes025_kb = InlineKeyboardMarkup()
perpes025_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

perpes05_kb = InlineKeyboardMarkup()
perpes05_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

perpes1_kb = InlineKeyboardMarkup()
perpes1_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

permef025_kb = InlineKeyboardMarkup()
permef025_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

permef05_kb = InlineKeyboardMarkup()
permef05_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

pershish2_kb = InlineKeyboardMarkup()
pershish2_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

perrab1_kb = InlineKeyboardMarkup()
perrab1_kb.add(InlineKeyboardButton('Канал🌊', callback_data='zakaz|Канал🌊'))

#/////////////////////////////////////////////////////////////////////////////////////GOLUBOVKA

golmef025_kb = InlineKeyboardMarkup()
golmef025_kb.add(InlineKeyboardButton('Памятник Трактору🚜', callback_data='zakaz|Памятник Трактору🚜'))

golshish2_kb = InlineKeyboardMarkup()
golshish2_kb.add(InlineKeyboardButton('Памятник Трактору🚜', callback_data='zakaz|Памятник Трактору🚜'))

#////////////////////////////////////////////////////////////////////////////////////GORISHNI PLAVNI

gpa05_kb = InlineKeyboardMarkup()
gpa05_kb.add(InlineKeyboardButton('Золотнишино🏘', callback_data='zakaz|Золотнишино🏘'))

gppes025_kb = InlineKeyboardMarkup()
gppes025_kb.add(InlineKeyboardButton('Феролит🚊', callback_data='zakaz|Феролит🚊'))

gpmef05_kb = InlineKeyboardMarkup()
gpmef05_kb.add(InlineKeyboardButton('Низы🌋', callback_data='zakaz|Низы🌋'))

gprab2_kb = InlineKeyboardMarkup()
gprab2_kb.add(InlineKeyboardButton('Центр🌆', callback_data='zakaz|Центр🌆'))

#//////////////////////////////////////////////////////////////////////////////////PODGORODNOE

podga025_kb = InlineKeyboardMarkup()
podga025_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podga05_kb = InlineKeyboardMarkup()
podga05_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podga1_kb = InlineKeyboardMarkup()
podga1_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podgpes015_kb = InlineKeyboardMarkup()
podgpes015_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podgpes025_kb = InlineKeyboardMarkup()
podgpes025_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podgpes05_kb = InlineKeyboardMarkup()
podgpes05_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podgpes1_kb = InlineKeyboardMarkup()
podgpes1_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podgshish1_kb = InlineKeyboardMarkup()
podgshish1_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

podgrab1_kb = InlineKeyboardMarkup()
podgrab1_kb.add(InlineKeyboardButton('Центр🌆', callback_data='zakaz|Центр🌆'))

#////////////////////////////////////////////////////////////////////////////////NOVOMOSKOVSK

nmpes015_kb = InlineKeyboardMarkup()
nmpes015_kb.add(InlineKeyboardButton('Лес🌲', callback_data='zakaz|Лес🌲'))

nmrab1_kb = InlineKeyboardMarkup()
nmrab1_kb.add(InlineKeyboardButton('Центр🌆', callback_data='zakaz|Центр🌆'))

#//////////////////////////////////////////////////////////////////////////////////JITOMIR

jtrab2_kb = InlineKeyboardMarkup()
jtrab2_kb.add(InlineKeyboardButton('Полевая🌾', callback_data='zakaz|Полевая🌾'))

#/////////////////////////////////////////////////////////////////////////////////SINELNIKOVO





#////////////////////////////////////////////////////////////////////////////PAYMENTS

afterpay_kb = InlineKeyboardMarkup(row_width=2)
afterpay_kb.add(InlineKeyboardButton('Отменить заказ', callback_data='cancelpay1'),InlineKeyboardButton('Посмотреть статус', callback_data='checkstatus'))

checkstatus_kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton('Помощь', callback_data='help')],
    [InlineKeyboardButton('Отменить заказ', callback_data='cancelpay1')],
    [InlineKeyboardButton('Продлить время бронирования', callback_data='longtime')],
    [InlineKeyboardButton('Обновить статус', callback_data = 'checkstatus')]
])

cancelpay1_kb = InlineKeyboardMarkup(row_width=2)
cancelpay1_kb.add(InlineKeyboardButton('Оплатить', callback_data='checkstatus'), InlineKeyboardButton('Отменить', callback_data='cancelpay2'))
