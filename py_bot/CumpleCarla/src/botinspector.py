import re
from flask import Flask, render_template   

app = Flask(__name__,
            template_folder="../www/templates",
            static_folder="../www/static")

#=================================================================
# FLASK : SHOW LOG
#=================================================================
@app.route("/")
def index():
    log_data = []
    with open("../cfg/app.log", 'r') as file:  
        for line in file:
            #Timestamp = pos 0, data = pos 3
            linia = [re.split(' - ', line)[0], re.split(' - ', line)[3]]
            log_data.append(linia)
          
    return render_template("index.html", log = log_data)

if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)