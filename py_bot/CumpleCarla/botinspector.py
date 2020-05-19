import re
from flask import Flask, render_template   
from flask_table import Table, Col

app = Flask(__name__)

#=================================================================
# FLASK : SHOW LOG
#=================================================================
class ItemTable(Table):
    #data = Col('Data')
    valor = Col('')

class Item(object):
    def __init__(self, valor):
        #self.data = data
        self.valor = valor

@app.route("/")
def espiar():
    items = []
    with open("app.log", 'r') as file:  
        for line in file:
            linia = re.split(' - ', line)
            items.append(Item(linia[3]))
            
    table = ItemTable(items)
    return render_template("index.html", table = table)

if __name__ == '__main__':
    app.run()