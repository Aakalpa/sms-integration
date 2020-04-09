# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = "AC803f894ec5fd72b07ff5873fc9452913"
auth_token = "23af0123f39cad286bfa7eb4df19029f"
client = Client(account_sid, auth_token)


message = client.messages.create(
    body="First message",
    from_="+15402742780",
     to='+9779861059159'
    # to="+9779845100204",
)

print(message.sid)


# +15402742780
# sid = AC803f894ec5fd72b07ff5873fc9452913
# tokern 23af0123f39cad286bfa7eb4df19029f
