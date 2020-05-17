from telegram.ext import Updater
import logging

#Updater
updater = Updater(token='1116840236:AAFP-BfnlE7mG969oESoSzymsMhQSMnwTz0', use_context=True)

dispatcher = updater.dispatcher

#Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Start message
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola!  Soc l'assistent virtual de l'agencia de viatges Flyonthewingsoflove. Porto mes de 30 anys ajudant a persones com tu a organitzar els seus viatges arrel del mon. Segueix les meves instruccions. Com et dius?")

updater.start_polling()                     