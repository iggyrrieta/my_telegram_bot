import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ForceReply

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

#Updater
updater = Updater(token='1116840236:AAFP-BfnlE7mG969oESoSzymsMhQSMnwTz0', use_context=True)

#Dispatcher
dispatcher = updater.dispatcher

ARGENTINA, BOLIVIA, BRASIL, CHILE, PERU = range(5)

PSW_ARGENTINA = '0'
PSW_BOLIVIA = '1'
PSW_BRASIL = '2'
PSW_CHILE = '3'
PSW_COLOMBIA = '4'
PSW_PERU = '5'

#Commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, "+ update.message.from_user.first_name+"!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soc el teu assistent personal de l'agència de viatges virtual *FLYONTHEWINGSOFLOVE*", parse_mode=telegram.ParseMode.MARKDOWN)     
    context.bot.send_message(chat_id=update.effective_chat.id, text="Porto més de 30 anys organitzant viatges virtuals arreu del món")  
    context.bot.send_message(chat_id=update.effective_chat.id, text="Segueix les meves instruccions i viatjarem allà on vulguis. En qualsevol moment del viatje, pots utilitzat la paraula clau /ajuda per contactar amb un dels nostres agents")  
    context.bot.send_message(chat_id=update.effective_chat.id, text="Començem?") 

def destinacions(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Argentina - /argentina\nBolivia - /bolivia\nBrasil - /brasil\nChile - /chile\nColombia - /colombia\nPerú - /peru")

def ajuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fes click al següent enllaç per posar-te en contacte amb un dels nostres agents")
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")

#Quiz
def argentina(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenida a *Argentina*, boluda!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Esperamos que pases un tiempo rebueno acá", parse_mode=telegram.ParseMode.MARKDOWN)

def bolivia(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Cap a *Bolivia*!", parse_mode=telegram.ParseMode.MARKDOWN)

def brasil(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bem vindo ao *Brasil*!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nós estávamos esperando por você, detetive", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Um crime foi cometido. Precisamos da sua ajuda para resolvê-lo", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Enviamos todas as informações para o seu apartamento", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Quando você descobrir a cena do crime, o assassino e a arma do crime, envie todos os dados para o e-mail do inspetor-chefe. Ele saberá o que fazer", parse_mode=telegram.ParseMode.MARKDOWN) 
    context.bot.send_message(chat_id=update.effective_chat.id, text="Muita sorte", parse_mode=telegram.ParseMode.MARKDOWN)
    #password = context.bot.send_message(update.effective_chat.id, text='Password', reply_markup=ForceReply())
    #if password != PSW_BRASIL:
    #    password = context.bot.send_message(update.effective_chat.id, 'Password', reply_markup=ForceReply())

#Text message
def echo(update, context):
    if (update.message.text.lower() == 'si') or (update.message.text.lower() == 'suuuh') or (update.message.text.lower() == 'yes') or (update.message.text.lower() == 'vale') or (update.message.text.lower() == 'ok') or (update.message.text.lower() == 'goes') or (update.message.text.lower() == 'groes'):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Genial!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="A continuació tens el llistat de les destinacions que offerim:")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Argentina - /argentina\nBolivia - /bolivia\nBrasil - /brasil\nChile - /chile\nColombia - /colombia\nPerú - /peru")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Fes click a sobre del lloc a on vulguis anar. Per tonar a accedir a aquest llistat utilitza la paraula clau /destinacions")
    
    elif (update.message.text == 'No') or (update.message.text == 'no'):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Doncs que et petin")  
    
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ho sento, no t'he entès")     

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

destinacions_handler = CommandHandler('destinacions', destinacions)
dispatcher.add_handler(destinacions_handler)

ajuda_handler = CommandHandler('ajuda', ajuda)
dispatcher.add_handler(ajuda_handler)

argentina_handler = CommandHandler('argentina', argentina)
dispatcher.add_handler(argentina_handler)

bolivia_handler = CommandHandler('bolivia', bolivia)
dispatcher.add_handler(bolivia_handler)

brasil_handler = CommandHandler('brasil', brasil)
dispatcher.add_handler(brasil_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()                     