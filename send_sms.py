# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9f684b45878b208f009f7b61b1a42ead'
auth_token = '3dd9a1a5adcd73fead476615a3506fd4'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14136501745',
                     to='+14132659744'
                 )

print(message.sid)
