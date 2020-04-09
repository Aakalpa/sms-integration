# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request

# from twilio import twiml

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


# @app.route("/sms", methods=["GET", "POST"])
# def sms():
#     number = request.form["From"]
#     message_body = request.form["Body"]

#     # resp = twiml.Response()
#     # resp.message("Hello {}, you said: {}".format(number, message_body))
#     print(number, message_body)
#     return "hello"


@app.route("/sms", methods=["GET", "POST"])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message("Your message has been received")
    print("data", request.data)
    print("args", request.args)
    print("form", request.form)
    print("values", request.values)

    return str(resp)

@app.route("/", methods=["GET", "POST"])
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5001,debug=True)
