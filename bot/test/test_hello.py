import bot.config
bot.config.TWILIO_ACCOUNT_SID = 'TEST'

from bot.hello import handler

test_event_1 = {
    'body': '',
}
test_event_2 = {
    'body': 'AccountSid=TEST&Body=Foobar'
}
test_cxt = {}

def test_handler_failure():
    ret = handler(test_event_1, test_cxt)
    assert ret.get('statusCode') == 404

'''
def test_handler_success():
    ret = handler(test_event_2, test_cxt)

    assert ret.get('statusCode') == 200
    assert ret.get('headers', {}).get('Content-Type') == 'text/xml'
    #assert ret.get('body', '') == '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Looking you up, fam...</Message></Response>'
'''
