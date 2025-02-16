import os
from twilio.rest import Client


client=Client("ACd2678b3ed40b6cbded4c0e65a3b6878b","9ec757b65a77f794d952ed0739d892ff")

#client.messages.create(to =["+917045204717"],from_ ="+12172698302",body="Hello")


no="+917045204717"
msg="helloooo"
client.messages.create(to =[no],from_ ="+12172698302",body=msg)