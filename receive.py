# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, render_template, jsonify
import json
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import environ
env = environ.Env()

environ.Env.read_env()

app = Flask(__name__)


@app.route("/",methods = ["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/send",methods = ["POST"])
def send():
    return render_template("send.html")

@app.route('/sendstatus',methods = ["POST"])
def send_status():
    account_sid = env("account_sid")
    auth_token = env("auth_token")
    account_sid = request.form.get("account_sid")
    auth_token = request.form.get("auth_token")
    client = Client(account_sid, auth_token)

    send_ph_no = request.form.get("send_ph_no")
    receive_ph_no = request.form.get("receive_ph_no")
    msg = request.form.get("msg")

    message = client.messages.create(
        body= msg,
        # from_="+15402742780",
        from_=send_ph_no,
        # to='+9779861059159'
        to=receive_ph_no
    )
    print(message.sid)
    sid = message.sid
    temp = {
        'sent from' : send_ph_no,
        'send to' : receive_ph_no,
        'msg' : msg,
        'sid' : sid
    }
    with open('send.txt','a') as f:
        json.dump(temp,f)
    return jsonify(temp)

@app.route("/sms", methods=["GET","POST"])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message("Your message has been received")

    # print("form", request.form)
    received_info = request.form
    with open("received.txt","a") as f:
    	json.dump(received_info,f)
    return json.dumps(received_info)

@app.route("/receive",methods = ["GET","POST"])
def receive():
    temp = [json.loads(line) for line in open('received.txt','r')]
    return json.dumps(temp)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5001,debug=True)
