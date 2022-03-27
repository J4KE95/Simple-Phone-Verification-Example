import time
import random
import twilio
from twilio.rest import Client
import config

account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)



def sms () :
  sendto = input("Enter the number you want the message sent to. (Use International Format. EG: +1) ")
  code = str(random.randint(1000, 9999))
  smsbody = "Your Verification Code Is: " + code 
  message = client.messages.create(
    to = sendto,
    from_ = "+18173306088",
    body = smsbody )
  print(message.sid)
  verify = input("Please Enter The Code You Were Sent: ")
  if verify == code :
      print("Verification Successful!")

def select () :
  print("Press 1 To Send Verification Code")
  selection = input("Please Choose An Option: ")
  if selection == "1" :
    sms()
  else :
    print("Invalid selection!")
    time.sleep(2)
    select()

select()