from bot.twilio_helpers import parse_body

sample_body = 'ToCountry=US&ToState=XX&SmsMessageSid=XXX&NumMedia=0&ToCity=XXX&FromZip=XXX&SmsSid=XXX&FromState=XX&SmsStatus=received&FromCity=XXX&Body=TEST&FromCountry=US&To=%2B10000000000&ToZip=XXXXX&NumSegments=1&MessageSid=XXX&AccountSid=TEST_SID&From=%2B10000000000&ApiVersion=2010-04-01'

def test_parse_body():
    dict_ = parse_body(sample_body)

    assert isinstance(dict_, dict)
    assert dict_.get('AccountSid') == 'TEST_SID'
