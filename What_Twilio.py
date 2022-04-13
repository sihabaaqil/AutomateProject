from twilio.rest import Client

account_sid="ACd1f32b49c534c82fb9f19816a49f4dfa"
auth_token="c689dd14a57d8c460309b0b929b0e1c3"
client=Client(account_sid,auth_token)
from_whatapp_number = 'whatapp:+1 415 523 8886'
to_whatapp_number ='whatapp:+919944380786'
client.messages.create(
    body="Hi",
    from_=from_whatapp_number,
    to=to_whatapp_number)