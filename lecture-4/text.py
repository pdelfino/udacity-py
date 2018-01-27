from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe7d94a4fdbf27e5f904e213207b4dbdb"

# Your Auth Token from twilio.com/console
auth_token  = "32f56018ad6a94749c0bc6bc3eb535b6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+31993547769", 
        from_="+552731800439",
            body="Hello from Python!")

print (message.sid)
