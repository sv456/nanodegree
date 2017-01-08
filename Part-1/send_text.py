from twilio.rest import TwilioRestClient

account_sid = "AC7d407081dd894f18c11445ece4469f67" # Your Account SID from www.twilio.com/console
auth_token  = "d3cfae385dcf1b4e0b75336526d6ee68"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+919742392140",    # Replace with your phone number
    from_="+12407506108") # Replace with your Twilio number

print(message.sid)
