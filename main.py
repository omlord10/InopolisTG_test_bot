import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


TOKEN = '6055601786:AAHhzFsugIwKzgqFvwR-P_GCzdXtSEAfLUU'

WEBHOOK_HOST = 'ef39cbeb-cc4d-4817-b363-c41d598059ad'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 80

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    return SendMessage(msg.chat.id, 'Hello!')


@dp.message_handler()
async def echo(msg: types.Message):
    return SendMessage(msg.chat.id, msg.text)


if __name__ == '__main__':
    start_webhook(
    dispatcher=dp,
    webhook_path=WEBHOOK_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host=WEBAPP_HOST,
    port=WEBAPP_PORT
    )
