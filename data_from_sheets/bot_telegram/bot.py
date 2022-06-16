import os
import time

from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

load_dotenv()

env_path = 'D:/my_prjcts/CanalService/data_from_sheets/bot_telegram/.env'

load_dotenv(dotenv_path=env_path)


def bot(order):
    """
    Отправка уведомления о статусе заказа.
    """
    status = 'просрочен'
    TOKEN = os.environ.get('TOKEN')
    bot = Bot(token=TOKEN)
    chat_id = os.environ.get('CHAT_ID')
    text = f'Good Day, заказ № {order} - {status}!'
    bot.send_message(chat_id, text)
    time.sleep(5)

    # updater = Updater(token=TOKEN)

    # def send_notification(update, context):
    #     chat = update.effective_chat
    #     name = update.message.chat.first_name
    #     context.bot.send_message(
    #         chat_id=chat.id,
    #         text=f'Good Day, {name}, заказ {order} - {status}!',
    #         )

    # updater.dispatcher.add_handler(CommandHandler('start', send_notification))
