from twilio.twiml.messaging_response import MessagingResponse

def hello_new_user():
    resp = MessagingResponse()
    resp.message(
'''
🎉 🎈🎂 🍾 🎊 🍻 💃 
Welcome to StrongBot, your very own, digital personal-trainer.

To get started, reply with:
    Start or s
''')

    return resp

def start_workout():
    resp = MessagingResponse()
    resp.message(
'''
''')
    return resp

def send_more_info(info):
    resp = MessagingResponse()
    resp.message(info)
    return resp

def error_msg():
    resp = MessagingResponse()
    resp.message(
'''
''')
    return resp
