import logging

from bot.bot_helpers import find_user, \
    parse_response, \
    get_info 
from bot.config import TWILIO_ACCOUNT_SID
from bot.enums import UserStatus, SupportedCmds
from bot.twilio_helpers import parse_body
from bot.responses import hello_new_user, \
    send_more_info, \
    start_workout, \
    error_msg

logger = logging.getLogger()
logger.setLevel(logging.INFO)

error_resp = {
    'statusCode': 404,
}

def handler(event, context):
    params = parse_body(event.get('body', ''))

    if params.get('AccountSid', None) != TWILIO_ACCOUNT_SID:
        return error_resp

    user_status, ddb = find_user(params)

    if user_status == UserStatus.NO_NUMBER:
        return error_resp
    elif user_status == UserStatus.NEW_USER:
        resp = hello_new_user()
    else:
        u_resp = parse_response(params)
        if u_resp in SupportedCmds.INFO:
            resp = send_more_info(get_info())
        elif u_resp in SupportedCmds.GET_STARTED:
            resp = start_workout()
        else:
            resp = error_msg()

    return {
        'headers': {
            'Content-Type': 'text/xml'
        },
        'statusCode': 200,
        'body': str(resp),
    } 
