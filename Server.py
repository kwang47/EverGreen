from flask import Flask, render_template, request
from redis import Redis
import smtplib



app = Flask(__name__)
redis = Redis(host='redis', port=6379)
localdatabase = []

@app.route('/')
def hello():
    redis.incr('hits')
    return render_template('index.html')



@app.route('/alarm', methods= ['GET','POST'])
def alarm():
    if request.method == 'POST':

        with open(r'templates/alarm.html', 'r') as file:
            userdata= request.form.to_dict()
            localdatabase.append(userdata)
            data = file.read()
            data = data.replace('<div ip="REPACE"></div><br>', '<label for="fname">'+userdata['Category']+'</label><input type="text" id="whoami'+str(len(localdatabase))+'value" name="firstname" placeholder="Spending"><div class="w3-light-grey"><p class="w3-grey" id="whoami'+str(len(localdatabase))+'bar" style="height:24px;width:0%" >0$/'+userdata['Limit']+'</p></div><br><button class="w3-button w3-green" id="whoami'+str(len(localdatabase))+'" onclick="move(this.id)">Click Me</button><br> <div ip="REPACE"></div><br>')
            file.close()
        print("hi", flush=True)
        print(request.form.to_dict() , flush=True)
        with open(r'templates/alarm.html', 'w') as file:
            file.write(data)

    return render_template('alarm.html')
@app.post('/email')
def email():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("kevintestme@proton.me", "B3?xE#p2bB,+L6w")

    # message to be sent
    message = localdatabase[0]['Message']
    sent = localdatabase[0]['Email']
    # sending the mail
    s.sendmail("kevintestme@proton.me", sent, message)

    # terminating the session
    s.quit()

    print("--------", flush=True)
    return ('', 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)