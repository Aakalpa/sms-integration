# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, render_template
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)



@app.route("/send")
def send():
    return render_template("send.html")

@app.route('/sendstatus',methods = ["POST"])
def send_status():
    account_sid = "AC803f894ec5fd72b07ff5873fc9452913"
    auth_token = "23af0123f39cad286bfa7eb4df19029f"
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
    return render_template("sendstatus.html",send_ph_no=send_ph_no,receive_ph_no=receive_ph_no,msg=msg,sid=sid)

@app.route("/sms", methods=["GET", "POST"])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message("Your message has been received")

    # print("form", request.form)
    received_info = request.form
    # return none
    return render_template("receive.html",received_msg = received_info)

@app.route("/", methods=["GET", "POST"])
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5001,debug=True)
