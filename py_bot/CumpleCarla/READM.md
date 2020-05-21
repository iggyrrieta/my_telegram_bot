# Cumple Carla

Python **BOT** creado para el cumple de Carla.


## Instalación

1. **Clonar repositorio :** `git clone https://github.com/iggyrrieta/my_telegram_bot`

2. **Ir a carpeta Cumple carla** : `cd my_telegram_bot/py_bot/CumpleCarla`

3. **Instalar requisitos :**
   
    1. **Para trabajar en local :** `pip install -r requirements_local.txt`
    
    2. **Para trabajar en web :** `pip install -r requirements_web.txt`
    
        > Básicamente estos requisitiso son:
        >
        > ​				librerias para trabajar en local : telegram, python-telegram-bot
        >
        > ​				librerias para trabajar en web : anteriores + flask


## Funcionamiento

El bot se puede arrancar desde terminal en local o desde web.


### Bot en local

1. **Abrir terminal**
2. **Ir a carpeta :** `cd my_telegram_bot/py_bot/CumpleCarla/src`
3. **Arrancar bot :** `python bot.py`
4. **Hablar con el bot desde telegram :** El bot se llama **@flyonthewingsoflovebot**

> Observar logs en `cfg/app.log`, para seguir funcionamiento del bot. El log contiene info de la última sesión.

### Bot en web