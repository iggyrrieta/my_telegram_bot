import re
from flask import Flask, render_template  
from apscheduler.schedulers.background import BackgroundScheduler 
from flask_socketio import SocketIO, emit

#=================================================================
# VARIABLES
#=================================================================
num_rows = 0
last_num_rows = 0

#=================================================================
# CONFIG
#=================================================================
app = Flask(__name__, template_folder="../www/templates")

socketio = SocketIO(app)

#=================================================================
# SCHEDULE JOBS
#=================================================================
def job():
    log_data = []
    global num_rows
    global last_num_rows

    with open("../cfg/app.log", 'r') as file:  
        for line in file:
            #Timestamp = pos 0, data = pos 3
            linia = [re.split(' - ', line)[0], re.split(' - ', line)[3]]
            log_data.append(linia)
            num_rows += 1
            
    
    if num_rows > last_num_rows:
        #job emits on websocket
        socketio.emit('logger',log_data, broadcast=True)
        last_num_rows = num_rows
        num_rows = 0
    else:
        num_rows = 0

scheduler = BackgroundScheduler()
running_job = scheduler.add_job(job, 'interval', seconds=1, max_instances=1)
scheduler.start()

#=================================================================
# PUBLISH
#=================================================================
@app.route("/")
def index():          
    return render_template("index.html")


#=================================================================
# MAIN
#=================================================================
if __name__ == '__main__':
    socketio.run(app,host= '192.168.1.86', port=8080, debug=False)