import logging

from bot.config import TWILIO_ACCOUNT_SID
from bot.twilio_helpers import parse_body
from json import dumps
from twilio.twiml.messaging_response import MessagingResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    params = parse_body(event.get('body', ''))
    if params.get('AccountSid', None) != TWILIO_ACCOUNT_SID:
        return {
            'statusCode': 404,
        }

    resp = MessagingResponse()
    body = params.get('Body', '').lower()
    if body == 'help':
        resp.message('Welcome to StrongBot!')
    else:
        resp.message('Looking you up, fam...')

    return {
        'headers': {
            'Content-Type': 'text/xml,'
        },
        'statusCode': 200,
        'body': str(resp),
    } 
