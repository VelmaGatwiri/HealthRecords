import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC172ebfa84ac742f363ce9856dea4e545'
auth_token = '9d1895c6e050b343455e5a16423fda21'
client = Client(account_sid, auth_token)


def send_sms(user_code, Phone_Number):
    message = client.messages.create(
    body=f'Hello! Your user and verification code is {user_code}',
    from_='+16165800880',
    to=f'{Phone_Number}'
    )

    print(message.sid)
