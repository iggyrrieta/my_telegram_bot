import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, ConversationHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ForceReply, ReplyKeyboardRemove
#======================
# Logging
#======================
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    #filename='app.log',
                    filemode='w', 
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger("FlyOn Carla")

#======================
# GLOVBAL VARIABLES
#======================
DESTINACIONS, INICI, AJUDA, ARG_PROVA, BOL_PROVA, BRA_PROVA, COL_PROVA, PER_PROVA, XIL_PROVA = range(9)

PASS_ARGENTINA = 'che'
PASS_BOLIVIA = 'stop'
PASS_BRASIL = 'VIVAOBRASIL'
PASS_COLOMBIA = '30'
PASS_PERU = 'cobait'
PASS_XILE = 'AGJFBHCEIKD'

OK_ARG = ''
OK_BOL = ''
OK_BRA = ''
OK_COL = ''
OK_PER = ''
OK_XIL = ''

#=================================================================
# BASIC COMMANDS
#=================================================================
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, "+ update.message.from_user.first_name+"!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soc el teu assistent personal de l'agència de viatges virtual *FLYONTHEWINGSOFLOVE*", parse_mode=telegram.ParseMode.MARKDOWN)     
    context.bot.send_message(chat_id=update.effective_chat.id, text="Porto més de 30 anys organitzant viatges virtuals arreu del món")  
    context.bot.send_message(chat_id=update.effective_chat.id, text="Segueix les meves instruccions i viatjarem allà on vulguis")  
    context.bot.send_message(chat_id=update.effective_chat.id, text="Començem?") 
    #LOG
    logger.info("[START] Usuari %s: ha iniciat una conversacio", update.message.from_user.first_name)

    return INICI

def cancel(update, context):
    user = update.message.from_user
    #LOG
    logger.info("[EXIT] Usuari %s ha cancelat la conversacio", user.first_name)
    update.message.reply_text('Adeu siau!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    #LOG
    logger.warning('Update "%s" ha causat un error inesperat "%s"', update, context.error)


#=================================================================
# CHECK POINTS
#=================================================================
def check_inici(update, context):

    if ((update.message.text.lower() == 'si') or
       (update.message.text.lower() == 'sí') or
       (update.message.text.lower() == 'suuuh') or 
       (update.message.text.lower() == 'yes') or
       (update.message.text.lower() == 'yeah') or 
       (update.message.text.lower() == 'vamos') or  
       (update.message.text.lower() == 'vale') or 
       (update.message.text.lower() == 'ok')):

       context.bot.send_message(chat_id=update.effective_chat.id, text="Genial!")  
       context.bot.send_message(chat_id=update.effective_chat.id, text="A continuació tens el llistat de les destinacions que offerim:")
       context.bot.send_message(chat_id=update.effective_chat.id, text="Argentina - /argentina\nBolivia - /bolivia\nBrasil - /brasil\nColombia - /colombia\nPerú - /peru\nXile - /xile")
       context.bot.send_message(chat_id=update.effective_chat.id, text="Fes click a sobre del lloc a on vulguis anar. Per tonar a accedir a aquest llistat utilitza la paraula clau /destinacions")
       context.bot.send_message(chat_id=update.effective_chat.id, text="Un cop hagis començat el teu viatge, pots consultar el teu itinerari a /itinerari")
       context.bot.send_message(chat_id=update.effective_chat.id, text="En qualsevol moment del viatje, pots utilitzat la paraula clau /ajuda per contactar amb un dels nostres agents")  
       #LOG
       logger.info("[CHECK INICI] Usuari %s ha escrit --> %s", update.message.from_user.first_name, update.message.text)  

       return 0
    
    elif ((update.message.text.lower() == 'goes') or 
       (update.message.text.lower() == 'groes')):

       context.bot.send_message(chat_id=update.effective_chat.id, text="Moroes!")  
       context.bot.send_message(chat_id=update.effective_chat.id, text="A continuació tens el llistat de les destinacions que offerim:")
       context.bot.send_message(chat_id=update.effective_chat.id, text="Argentina - /argentina\nBolivia - /bolivia\nBrasil - /brasil\nColombia - /colombia\nPerú - /peru\nXile - /xile")
       context.bot.send_message(chat_id=update.effective_chat.id, text="Fes click a sobre del lloc a on vulguis anar. Per tonar a accedir a aquest llistat utilitza la paraula clau /destinacions")
       context.bot.send_message(chat_id=update.effective_chat.id, text="Un cop hagis començat el teu viatge, pots consultar el teu itinerari a /itinerari")
       context.bot.send_message(chat_id=update.effective_chat.id, text="En qualsevol moment del viatje, pots utilitzat la paraula clau /ajuda per contactar amb un dels nostres agents")  
       #LOG
       logger.info("[CHECK INICI] Usuari %s ha escrit --> %s", update.message.from_user.first_name, update.message.text)  

       return 0
    
    elif ((update.message.text == 'No') or
         (update.message.text == 'no')):

        context.bot.send_message(chat_id=update.effective_chat.id, text="Doncs que et petin")  
    
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ho sento, no t'he entès")   

    #LOG
    logger.info("[CHECK INICI] Usuari %s ha escrit --> %s", update.message.from_user.first_name, update.message.text)  

def check_argentina(update, context):

    global OK_ARG 

    if update.message.text.lower() == PASS_ARGENTINA:
        #LOG
        logger.info("[CHECK ARGENTINA] Usuari %s ha ENCERTAT password ARGENTINA --> %s", update.message.from_user.first_name, update.message.text) 

        OK_ARG = update.message.text.lower()
        context.bot.send_message(chat_id=update.effective_chat.id, text="*Correcte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        
        if ((OK_ARG==PASS_ARGENTINA) and (OK_BOL==PASS_BOLIVIA) and (OK_BRA==PASS_BRASIL) \
            and (OK_COL==PASS_COLOMBIA) and (OK_PER==PASS_PERU) and (OK_XIL==PASS_XILE)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Felicitats 🎉🎉🎉", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="El teu viatge a arribat a la fi", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Esperem que hagis gaudit del itinerari", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Si us plau, fes click al següent enllaç per omplir una petita enquesta sobre la teva experiència", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")  
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Recorda que pots veure el teu itinerari a /itinerari i les nostres destinacions a /destinacions", parse_mode=telegram.ParseMode.MARKDOWN)
        
        return 0

    else:
        #LOG
        logger.info("[CHECK ARGENTINA] Usuari %s ha FALLAT password ARGENTINA --> %s", update.message.from_user.first_name, update.message.text) 

        context.bot.send_message(chat_id=update.effective_chat.id, text="*Incorrecte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Argentina:*", parse_mode=telegram.ParseMode.MARKDOWN)

def check_brasil(update, context):

    global OK_BRA

    if update.message.text.upper() == PASS_BRASIL:
        #LOG
        logger.info("[CHECK BRASIL] Usuari %s ha ENCERTAT password BRASIL --> %s", update.message.from_user.first_name, update.message.text) 

        OK_BRA = update.message.text.upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text="*Correcte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        if ((OK_ARG==PASS_ARGENTINA) and (OK_BOL==PASS_BOLIVIA) and (OK_BRA==PASS_BRASIL) \
            and (OK_COL==PASS_COLOMBIA) and (OK_PER==PASS_PERU) and (OK_XIL==PASS_XILE)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Felicitats 🎉🎉🎉", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="El teu viatge a arribat a la fi", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Esperem que hagis gaudit del itinerari", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Si us plau, fes click al següent enllaç per omplir una petita enquesta sobre la teva experiència", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")  
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Recorda que pots veure el teu itinerari a /itinerari i les nostres destinacions a /destinacions", parse_mode=telegram.ParseMode.MARKDOWN)
        
        return 0

    else:
        #LOG
        logger.info("[CHECK BRASIL] Usuari %s ha FALLAT password BRASIL --> %s", update.message.from_user.first_name, update.message.text) 

        context.bot.send_message(chat_id=update.effective_chat.id, text="*Incorrecte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Brasil:*", parse_mode=telegram.ParseMode.MARKDOWN)

def check_bolivia(update, context):

    global OK_BOL 

    if update.message.text.lower() == PASS_BOLIVIA:
        #LOG
        logger.info("[CHECK BOLIVIA] Usuari %s ha ENCERTAT password BOLIVIA --> %s", update.message.from_user.first_name, update.message.text) 

        OK_BOL = update.message.text.lower()
        context.bot.send_message(chat_id=update.effective_chat.id, text="*Correcte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        if ((OK_ARG==PASS_ARGENTINA) and (OK_BOL==PASS_BOLIVIA) and (OK_BRA==PASS_BRASIL) \
            and (OK_COL==PASS_COLOMBIA) and (OK_PER==PASS_PERU) and (OK_XIL==PASS_XILE)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Felicitats 🎉🎉🎉", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="El teu viatge a arribat a la fi", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Esperem que hagis gaudit del itinerari", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Si us plau, fes click al següent enllaç per omplir una petita enquesta sobre la teva experiència", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")  
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Recorda que pots veure el teu itinerari a /itinerari i les nostres destinacions a /destinacions", parse_mode=telegram.ParseMode.MARKDOWN)
        
        return 0

    else:
        #LOG
        logger.info("[CHECK BOLIVIA] Usuari %s ha FALLAT password BOLIVIA --> %s", update.message.from_user.first_name, update.message.text) 

        context.bot.send_message(chat_id=update.effective_chat.id, text="*Incorrecte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Bolivia:*", parse_mode=telegram.ParseMode.MARKDOWN)

def check_colombia(update, context):

    global OK_COL 

    if update.message.text == PASS_COLOMBIA:
        #LOG
        logger.info("[CHECK COLOMBIA] Usuari %s ha ENCERTAT password COLOMBIA --> %s", update.message.from_user.first_name, update.message.text) 

        OK_COL = update.message.text
        context.bot.send_message(chat_id=update.effective_chat.id, text="*Correcte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        if ((OK_ARG==PASS_ARGENTINA) and (OK_BOL==PASS_BOLIVIA) and (OK_BRA==PASS_BRASIL) \
            and (OK_COL==PASS_COLOMBIA) and (OK_PER==PASS_PERU) and (OK_XIL==PASS_XILE)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Felicitats 🎉🎉🎉", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="El teu viatge a arribat a la fi", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Esperem que hagis gaudit del itinerari", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Si us plau, fes click al següent enllaç per omplir una petita enquesta sobre la teva experiència", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")  
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Recorda que pots veure el teu itinerari a /itinerari i les nostres destinacions a /destinacions", parse_mode=telegram.ParseMode.MARKDOWN)
        
        return 0

    else:
        #LOG
        logger.info("[CHECK COLOMBIA] Usuari %s ha FALLAT password COLOMBIA --> %s", update.message.from_user.first_name, update.message.text) 

        context.bot.send_message(chat_id=update.effective_chat.id, text="*Incorrecte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Colombia:*", parse_mode=telegram.ParseMode.MARKDOWN)

def check_peru(update, context):

    global OK_PER

    if update.message.text.lower() == PASS_PERU:
        #LOG
        logger.info("[CHECK PERU] Usuari %s ha ENCERTAT password PERU --> %s", update.message.from_user.first_name, update.message.text) 

        OK_PER = update.message.text.lower()
        context.bot.send_message(chat_id=update.effective_chat.id, text="*Correcte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        if ((OK_ARG==PASS_ARGENTINA) and (OK_BOL==PASS_BOLIVIA) and (OK_BRA==PASS_BRASIL) \
            and (OK_COL==PASS_COLOMBIA) and (OK_PER==PASS_PERU) and (OK_XIL==PASS_XILE)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Felicitats 🎉🎉🎉", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="El teu viatge a arribat a la fi", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Esperem que hagis gaudit del itinerari", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Si us plau, fes click al següent enllaç per omplir una petita enquesta sobre la teva experiència", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")  
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Recorda que pots veure el teu itinerari a /itinerari i les nostres destinacions a /destinacions", parse_mode=telegram.ParseMode.MARKDOWN)
        
        return 0

    else:
        #LOG
        logger.info("[CHECK PERU] Usuari %s ha FALLAT password PERU --> %s", update.message.from_user.first_name, update.message.text) 

        context.bot.send_message(chat_id=update.effective_chat.id, text="*Incorrecte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Peru:*", parse_mode=telegram.ParseMode.MARKDOWN)

def check_xile(update, context):

    global OK_XIL 

    if update.message.text.upper() == PASS_XILE:
        #LOG
        logger.info("[CHECK XILE] Usuari %s ha ENCERTAT password XILE --> %s", update.message.from_user.first_name, update.message.text) 

        OK_XIL = update.message.text.upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text="*Correcte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        if ((OK_ARG==PASS_ARGENTINA) and (OK_BOL==PASS_BOLIVIA) and (OK_BRA==PASS_BRASIL) \
            and (OK_COL==PASS_COLOMBIA) and (OK_PER==PASS_PERU) and (OK_XIL==PASS_XILE)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Felicitats 🎉🎉🎉", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="El teu viatge a arribat a la fi", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Esperem que hagis gaudit del itinerari", parse_mode=telegram.ParseMode.MARKDOWN) 
            context.bot.send_message(chat_id=update.effective_chat.id, text="Si us plau, fes click al següent enllaç per omplir una petita enquesta sobre la teva experiència", parse_mode=telegram.ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")  
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Recorda que pots veure el teu itinerari a /itinerari i les nostres destinacions a /destinacions", parse_mode=telegram.ParseMode.MARKDOWN)
        
        return 0

    else:
        #LOG
        logger.info("[CHECK XILE] Usuari %s ha FALLAT password XILE --> %s", update.message.from_user.first_name, update.message.text) 

        context.bot.send_message(chat_id=update.effective_chat.id, text="*Incorrecte!*", parse_mode=telegram.ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Xile:*", parse_mode=telegram.ParseMode.MARKDOWN)


#=================================================================
# FLYONTHEWINDSOFLOVE COMMANDS
#=================================================================
def ajuda(update, context):
    #LOG
    logger.info("[AJUDA] Usuari %s: ha demanat ajuda!", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Fes click al següent enllaç per posar-te en contacte amb un dels nostres agents")
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")

def destinacions(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="A continuació tens el llistat de les destinacions que offerim:")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Argentina - /argentina\nBolivia - /bolivia\nBrasil - /brasil\nColombia - /colombia\nPerú - /peru\nXile - /xile")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fes click a sobre del lloc a on vulguis anar. Per tonar a accedir a aquest llistat utilitza la paraula clau /destinacions")

    #LOG
    logger.info("[DESTINACIONS] Usuari %s ha demanat veure destinacions", update.message.from_user.first_name)

def argentina(update, context):
    #LOG
    logger.info("[DESTINACIONS] Usuari %s esta a ARGENTINA", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenida a la *Argentina*, boluda!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Che, parece que se armó un quilombo en la aduana", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="El presidente Macri acaba de anunciar que cierra todas las fronteras a todos los pibes que no aman a la Argentina", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Para poder entrar, tenés que demostrar tu conocimiento del país, adivinando las palabras que dos agentes de la aduana pensaron para vos", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Podés comenzar la prueba aquí:", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Andáte!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Argentina:*", parse_mode=telegram.ParseMode.MARKDOWN)

    return ARG_PROVA

def bolivia(update, context):
    #LOG
    logger.info("[DESTINACIONS] Usuari %s esta a BOLIVIA", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Sembla que no has demanat el visat per tal de poder viatjar a *Bolivia*", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Desde FLYONTHEWINGSOFLOVE hem aconseguit accelerat els tràmits per obtenir el teu visat online. Però has de ser tu qui contacti amb el consulat per obtenir la clau d’activació.", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="A continuació et passem l’enllaç al seu call center", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Bolivia:*", parse_mode=telegram.ParseMode.MARKDOWN)

    return BOL_PROVA

def brasil(update, context):
    #LOG
    logger.info("[DESTINACIONS] Usuari %s esta a BRASIL", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Bem vindo ao *Brasil*!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nós estávamos esperando por você, detetive", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Um crime foi cometido. Precisamos da sua ajuda para resolvê-lo", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Enviamos todas as informações para o seu apartamento", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Quando você descobrir a cena do crime, o assassino e a arma do crime, envie todos os dados para o inspetor-chefe. Ele saberá o que fazer", parse_mode=telegram.ParseMode.MARKDOWN) 
    context.bot.send_message(chat_id=update.effective_chat.id, text="Muita sorte", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Brasil:*", parse_mode=telegram.ParseMode.MARKDOWN)

    return BRA_PROVA

def colombia(update, context):
    #LOG
    logger.info("[DESTINACIONS] Usuari %s esta a COLOMBIA", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenida a *Colombia*, mamita!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="El nostre agent local t'ha deixat un sobre al hotel", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Conté aquest missatge:", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="_Segueix les fotos del collage en línies rectes verticals o horitzontals (no diagonals) i descobreix què s’hi amaga_", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="_1. De la festassa de Sitges decideixes anar a UK, passant primer per Edimburg i després per Londres, on et quedes a dormir a casa la Nurifly. Decideixes tornar altre cop als parcs de Londres, tot i que després fas camí cap a l’aeroport on un avió et portarà en direcció cap al País Basc, on aniràs a parar a Plentzia_", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="_2. Partint d’un Sant Albert, passes per una mani de l’11 de Setembre però veus que després necessites passar un cap de setmana amb els físics esquiant. De totes formes el curs avança i toca a vegades fer presentacions. Això sí, sempre tornem al nostre dia de Sant Albert_", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="I aquesta direcció:", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://drive.google.com/drive/folders/1xi2Ey5zTBBGfmAPEvTDGbl_DFuFC4Itj?usp=sharing")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Colombia:*", parse_mode=telegram.ParseMode.MARKDOWN)

    return COL_PROVA

def peru(update, context):
    #LOG
    logger.info("[DESTINACIONS] Usuari %s esta a PERÚ", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Bona elecció! Jo sempre he volgut anar a *Perú*...", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Espera...", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hem rebut una notificació per part del nostre agent local a Perú", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sembla que, degut a la situació actual, la mobilitat a dins del país està restringida i no es pot viatjar lliurement", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="La seva recomenació és viatjar d'incògnit", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="No pateixis. Fes click al següent enllaç i un dels nostres agents t'ajudarà a triar un personatge òptim per viatjar sense problemes", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://meet.jit.si/FlyOnTheWingsOfLove")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Perú:*", parse_mode=telegram.ParseMode.MARKDOWN)

    return PER_PROVA

def xile(update, context):
    #LOG
    logger.info("[DESTINACIONS] Usuari %s esta a XILE", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Que viva *Chile*, huevones!", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Llegas justo a tiempo para el acto memorial por la muerte de Salvador Allende. Hemos organizado una lectura de poemas y hemos pedido a varios artistas internacionales que lean algunos versos", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="En el audio original aparecían ordenados por edad, pero parece que ha habido algún problema con la grabación y se han desordenado los versos", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ahí nomás te envío las pistas de audio para que nos ayudes a arreglarlo", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://drive.google.com/drive/u/1/folders/1shrVXFUUnZBlCuJVEuyw0IqRktsvPHy2", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Introdueix *PASSWORD Xile:*", parse_mode=telegram.ParseMode.MARKDOWN)

    return XIL_PROVA

def itinerari(update, context):
    #LOG
    logger.info("[ITINERARI] Usuari %s esta comprobant itinerari", update.message.from_user.first_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"*Itinerari*\nArgentina - {OK_ARG}\nBolivia - {OK_BOL}\nBrasil - {OK_BRA}\nColombia - {OK_COL}\nPerú - {OK_PER}\nXile - {OK_XIL}", parse_mode=telegram.ParseMode.MARKDOWN)

#=================================================================
# MAIN
#=================================================================
def main():
    '''START THE BOT
    '''

    #======================
    # Updater & dispatcher
    #======================
    #Updater : Create the Updater and pass it your bot's token.
    updater = Updater(token='1116840236:AAFP-BfnlE7mG969oESoSzymsMhQSMnwTz0', use_context=True)

    #Dispatcher : Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    #======================
    # Handlers
    #======================    
    handler_inicio = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            INICI: [MessageHandler(Filters.text, check_inici)]},
        fallbacks=[CommandHandler('exit', cancel)])

    handler_argentina = ConversationHandler(
        entry_points=[CommandHandler('argentina', argentina)],

        states={
            ARG_PROVA: [MessageHandler(Filters.text, check_argentina)]},
        fallbacks=[CommandHandler('exit', cancel)])

    handler_bolivia = ConversationHandler(
        entry_points=[CommandHandler('bolivia', bolivia)],

        states={
            BOL_PROVA: [MessageHandler(Filters.text, check_bolivia)]},
        fallbacks=[CommandHandler('exit', cancel)])

    handler_brasil = ConversationHandler(
        entry_points=[CommandHandler('brasil', brasil)],

        states={
            BRA_PROVA: [MessageHandler(Filters.text, check_brasil)]},
        fallbacks=[CommandHandler('exit', cancel)])
    
    handler_xile = ConversationHandler(
        entry_points=[CommandHandler('xile', xile)],

        states={
            XIL_PROVA: [MessageHandler(Filters.text, check_xile)]},
        fallbacks=[CommandHandler('exit', cancel)])
    
    handler_colombia = ConversationHandler(
        entry_points=[CommandHandler('colombia', colombia)],

        states={
            COL_PROVA: [MessageHandler(Filters.text, check_colombia)]},
        fallbacks=[CommandHandler('exit', cancel)])
    
    handler_peru = ConversationHandler(
        entry_points=[CommandHandler('peru', peru)],

        states={
            PER_PROVA: [MessageHandler(Filters.text, check_peru)]},
        fallbacks=[CommandHandler('exit', cancel)])

    dispatcher.add_handler(handler_inicio)
    dispatcher.add_handler(handler_argentina)
    dispatcher.add_handler(handler_bolivia)
    dispatcher.add_handler(handler_brasil)
    dispatcher.add_handler(handler_xile)
    dispatcher.add_handler(handler_colombia)
    dispatcher.add_handler(handler_peru)
    dispatcher.add_handler(CommandHandler('destinacions', destinacions))
    dispatcher.add_handler(CommandHandler('itinerari', itinerari))
    dispatcher.add_handler(CommandHandler('ajuda', ajuda))


    #======================
    # START BOT
    #======================
    #Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()