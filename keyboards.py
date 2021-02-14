from aiogram import types
import callback_data


welcome = types.InlineKeyboardMarkup(row_width=2)
item_aboutme = types.InlineKeyboardButton(text='ℹ️Обо мне', callback_data='welcome:about_me')
item_smth = types.InlineKeyboardButton(text='🏫 Контакты', callback_data='welcome:contacts')
item_news = types.InlineKeyboardButton(text='📩 Рассылка новостей', callback_data='welcome:news')
item_site = types.InlineKeyboardButton(text='🌐 Сайт гимназии', url='http://www.gymn-1.ru/news.php')
welcome.add(item_aboutme, item_smth, item_news)
welcome.add(item_site)

aboutme_1 = types.InlineKeyboardMarkup(row_width=1)
item_continue_aboutme_1 = types.InlineKeyboardButton(text='➡ Читать дальше', callback_data='aboutme_1:continue_aboutme_1')
item_backtomain = types.InlineKeyboardButton(text='🔙 Вернуться на главную', callback_data='aboutme_1:main')
aboutme_1.add(item_continue_aboutme_1)
aboutme_1.add(item_backtomain)

aboutme_2 = types.InlineKeyboardMarkup(row_width=1)
item_continue_aboutme_2 = types.InlineKeyboardButton(text='➡ Читать дальше', callback_data='aboutme_2:continue_aboutme_2')
aboutme_2.add(item_continue_aboutme_2)
aboutme_2.add(item_backtomain)

aboutme_3 = types.InlineKeyboardMarkup(row_width=1)
item_backtoprev = types.InlineKeyboardButton(text='⬅ На предыдущую', callback_data='aboutme_3:prev')
aboutme_3.add(item_backtoprev)
aboutme_3.add(item_backtomain)

contacts = types.InlineKeyboardMarkup(row_width=3)
item_tel = types.InlineKeyboardButton(text='☎ Телефон', callback_data='contacts:tel')
item_address = types.InlineKeyboardButton(text='🗺️ Наш адрес', callback_data='contacts:address')
item_email = types.InlineKeyboardButton(text='📧 E-mail', callback_data='contacts:email')
contacts.add(item_tel, item_address, item_email)
contacts.add(item_backtomain)

back_to_contacts = types.InlineKeyboardMarkup(row_width=1)
item_backtocontacts = types.InlineKeyboardButton(text='⬅ Назад', callback_data='backtocontacts:1')
back_to_contacts.add(item_backtocontacts)
back_to_contacts.add(item_backtomain)

address = types.InlineKeyboardMarkup(row_width=2)
item_map = types.InlineKeyboardButton(text='📍 На карте', callback_data='address:map')
address.add(item_map, item_backtocontacts)
address.add(item_backtomain)

address_map = types.InlineKeyboardMarkup(row_width=1)
item_address_backtomain = types.InlineKeyboardButton(text='🔙 Вернуться на главную', callback_data='address_map:main')
address_map.add(item_address_backtomain)

news_keyboard = types.InlineKeyboardMarkup(row_width=1)
item_full = types.InlineKeyboardButton(text='📰 Прочитать новость целиком', url='http://www.gymn-1.ru/news.php')
news_keyboard.add(item_full)

subscription = types.InlineKeyboardMarkup(row_width=1)
item_sub_backtomain = types.InlineKeyboardButton(text='🔙 Вернуться на главную', callback_data='sub:main')
subscription.add(item_sub_backtomain)

