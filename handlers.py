# -*- coding: utf-8 -*-
from aiogram.types import CallbackQuery, ParseMode
from main import bot, dp
from aiogram import types
import keyboards
from database import SqLighter

db=SqLighter('database.db')

@dp.message_handler(commands = ['start'])
async def welcome_message(message: types.Message):
    photo = open('images/001.jpg', 'rb')
    caption = f"<b>Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}!</b>\nВас приветствует бот классической гимназии №1 им.В.Г.Белинского г.Пензы"
    await bot.send_photo(message.chat.id, photo, caption, reply_markup=keyboards.welcome)

@dp.callback_query_handler(text='welcome:about_me')
async def about_me(call: CallbackQuery):
    photo = open('images/002.jpg', 'rb')
    caption = f"Я - <b>Пензенская классическая гимназия №1 им. В.Г. Белинского</b>, родилась в городе Пензе в туманной 235-летней дали по высочайшему указу царствующей тогда особы Екатерины Алексеевны, оставшейся в памяти народной покровительницей наук и искусств."
    await call.bot.send_photo(call.message.chat.id, photo, caption, reply_markup=keyboards.aboutme_1)

@dp.callback_query_handler(text='welcome:contacts')
async def contacts(call: CallbackQuery):
    text = 'Выберите нужное:'
    await bot.send_message(call.message.chat.id, text=text, reply_markup=keyboards.contacts)

@dp.callback_query_handler(text='welcome:news')
async  def sub_news(call: CallbackQuery):
    text = 'Вы можете подписаться на рассылку новостей, чтобы всегда быть в курсе событий, происходящих в гимназии\nНажмите /subscribe, чтобы подписаться,\n/unsubscribe, чтобы отписаться'
    await bot.send_message(call.message.chat.id, text=text, reply_markup=keyboards.subscription)

@dp.callback_query_handler(text_contains='backtocontacts')
async def back_to_contacts(call: CallbackQuery):
    text = 'Выберите нужное:'
    await call.message.edit_text(text=text, reply_markup=keyboards.contacts)

@dp.callback_query_handler(text='contacts:tel')
async def tel(call: CallbackQuery):
    text = f"<b>Контактный телефон</b>: (8-412) 66-09-10"
    await call.message.edit_text(text=text, reply_markup=keyboards.back_to_contacts)

@dp.callback_query_handler(text='contacts:email')
async def email(call: CallbackQuery):
    text = f"**E-mail**: `school01@guoedu.ru` "
    await call.message.edit_text(text=text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboards.back_to_contacts )

@dp.callback_query_handler(text='contacts:address')
async def address(call: CallbackQuery):
    text = f"<b>Наш адрес</b>: 440026. г. Пенза, ул. Красная, 54"
    await call.message.edit_text(text=text, reply_markup=keyboards.address)

@dp.callback_query_handler(text='address:map')
async def address_map(call: CallbackQuery):
    await bot.send_location(call.message.chat.id, latitude=53.185010, longitude=45.005417, reply_markup=keyboards.address_map)

@dp.callback_query_handler(text_contains="main")
async def welcome_message(call: CallbackQuery):
    photo = open('images/001.jpg', 'rb')
    caption = f"<b>Вы вернулись на главную</b>"
    await bot.send_photo(call.message.chat.id, photo, caption, reply_markup=keyboards.welcome)

@dp.callback_query_handler(text='aboutme_1:continue_aboutme_1')
async def continue_1(call: CallbackQuery):
    text = f"Сохраняя внешние черты минувшего - сводчатые окна и потолки, кованая, с затейливыми узорами, парадная лестница, строгий интерьер залов (здание гимназии - памятник истории и архитектуры России ХГХв.), - я не чураюсь технического прогресса. Синтез лучших классических черт прошлого и жестких требований дня сегодняшнего осуществляется не только во внешнем облике здания, но и во всех сферах деятельности учреждения. Возьмем, к примеру, современный учебный план. В нем риторика, латинский язык, логика, этикет, бальные танцы, хоровое пение, переплетное дело уживаются с вполне современными: психологией общения, социологией, делопроизводством - и применением новых информационных технологий в преподавании и управлении. Я, гимназия, всегда была законодательницей мод. На меня равнялись, мне завидовали, мною восхищались... Посмотрите на гимназистов сегодня: строгая форма, изысканные манеры, одухотворенные лица. Это краса, гордость и надежда земли Пензенской!"
    await call.message.reply(text=text, reply_markup=keyboards.aboutme_2)

@dp.callback_query_handler(text='aboutme_2:continue_aboutme_2')
async def continue_2(call: CallbackQuery):
    text = f"Вы спросите, как мне удается всегда быть на высоте? Очень просто. У истоков моей образовательной деятельности стояли такие мэтры, как И. Ульянов, В. Белинский, И. Лажечников, возглавлявший педагогический коллектив. Гимназия и сегодня продолжает их славное дело, являясь творческой лабораторией по апробированию личностно -ориентированного подхода к образованию, внедряя методику развивающего обучения по системе Д. Эльконина-В. Давыдова. Не удивляйтесь, что многое из лучшего, что есть в образовании Пензенской губернии, впервые появилось именно у нас: Попечительский совет, летопись попечителей, Совет гимназии, Совет бабушек, дни открытых дверей, участие в телекоммуникационных олимпиадах и Интернет-проектах... Порыв, дерзновение, напряженная работа, полная самоотдачи, -так рождается особая образовательная среда, пробуждающая в гимназистах и их наставниках жажду знания и творчества. Мне всегда везло на талантливых учеников. Их заслуги и титулы можно перечислять долго. Это и «неистовый» Виссарион, и филолог Буслаев, маршал Тухачевский, ученые, художники, писатели, музыканты, общественные деятели.... Сегодня этот ряд пополняется год от года. На Звездной карте гимназии зажигаются новые имена: поэтесса Яшина, член-корреспондент РАН Дмитриев, лауреат четырех Государственных премий Ю.М. Попов и многие другие. Конечно, это лишь некоторые сухие факты биографии, а душа моя - в моих воспитанниках, в моей истории, которая создается каждый день вот уже больше двухсот лет. Прошу любить и жаловать! <b>Классическая гимназия №1 имени В.Г. Белинского, г. Пенза.</b> Приезжайте, приходите, и все увидите сами!"
    await call.message.edit_text(text=text, reply_markup=keyboards.aboutme_3)

@dp.callback_query_handler(text='aboutme_3:prev')
async def backto_2(call: CallbackQuery):
    text = f"Сохраняя внешние черты минувшего - сводчатые окна и потолки, кованая, с затейливыми узорами, парадная лестница, строгий интерьер залов (здание гимназии - памятник истории и архитектуры России ХГХв.), - я не чураюсь технического прогресса. Синтез лучших классических черт прошлого и жестких требований дня сегодняшнего осуществляется не только во внешнем облике здания, но и во всех сферах деятельности учреждения. Возьмем, к примеру, современный учебный план. В нем риторика, латинский язык, логика, этикет, бальные танцы, хоровое пение, переплетное дело уживаются с вполне современными: психологией общения, социологией, делопроизводством - и применением новых информационных технологий в преподавании и управлении. Я, гимназия, всегда была законодательницей мод. На меня равнялись, мне завидовали, мною восхищались... Посмотрите на гимназистов сегодня: строгая форма, изысканные манеры, одухотворенные лица. Это краса, гордость и надежда земли Пензенской!"
    await call.message.edit_text(text=text, reply_markup=keyboards.aboutme_2)


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscription(message.from_user.id, True)
    await message.answer('✅ Вы успешно подписались на рассылку!')

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer('Вы не подписаны')
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer('❌ Вы отписались от рассылки')


@dp.message_handler(content_types=['text'])
async def any_text(message):
    answer = f'Меня не научили отвечать на такие сообщения 😢\nЕсли Вы хотите вернуться на главную страницу, используйте /start'
    await message.answer(answer)