import asyncio
import logging

from config import token
from aiogram import Bot, Dispatcher, executor
from parse import parse
from database import SqLighter
from keyboards import news_keyboard

db=SqLighter('database.db')

logging.basicConfig(level=logging.INFO)
bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot)


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        print('000')
        news = str(parse())
        text = f"🔔 На сайте опубликована новая запись!\n<b>{news}</b>"
        f=open('latest_news_id', 'b')
        latest_news = f.read()
        f.close()
        if latest_news != news:
            f = open('latest_news_id', 'w')
            f.write(news)
            f.close()
            subscriptions = db.get_subscriptions()
            for s in subscriptions:
                await bot.send_message(s[1], text=text, reply_markup=news_keyboard)


if __name__ == '__main__':
    from handlers import dp
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    executor.start_polling(dp, skip_updates=True)