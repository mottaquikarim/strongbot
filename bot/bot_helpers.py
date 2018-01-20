from bot.config import AIRTABLE_API_KEY, AIRTABLE_BASE_KEY
from bot.enums import UserStatus
from bot.models.user import User
from bot.models.airtable import Airtable
import urllib.parse

def find_user(params):
    user_ph = params.get('From', None)

    if not user_ph:
        return UserStatus.NO_NUMBER, None

    u = User()
    user_ph = urllib.parse.unquote(user_ph)

    user_logs = u.search_by_number(
        phonenumber=user_ph,
    )

    if not user_logs:
        u.create_row(
            phonenumber=user_ph, 
        )

        return UserStatus.NEW_USER, u


    return UserStatus.EXISTING_USER, u

def parse_response(params):
    resp = params.get('Body', None)
    if not resp:
        return None

    return urllib.parse.unquote(resp).lower()

def get_airtable():
    return Airtable(
        api_key=AIRTABLE_API_KEY,
        base_key=AIRTABLE_BASE_KEY,
    )

def get_meta():
    t = get_airtable()
    data = t.get_tabledata(endpt=t.meta)

    return data

def get_info():
    d = get_meta()
    return Airtable.query_data(d, 'Name', 'About')
