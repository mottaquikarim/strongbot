from bot.enums import UserStatus
from bot.models.airtable import Airtable

from bot.bot_helpers import find_user, \
    parse_response, \
    get_airtable, \
    get_meta, \
    get_info

def test_find_user():
    a, b = find_user({})

    assert a == UserStatus.NO_NUMBER
    assert b is None


    a, b = find_user({
        'From': '+1XXXYYYZZZZ', 
    })

    assert a == UserStatus.NEW_USER

    a, b = find_user({
        'From': '+1XXXYYYZZZZ', 
    })

    assert a == UserStatus.EXISTING_USER

def test_parse_response():
    pr = parse_response({})

    assert pr is None

    pr = parse_response({
        'Body': 'FooBaR',
    })

    assert pr == 'foobar'

def test_get_airtable():
    at = get_airtable()
    assert isinstance(at, Airtable)

def test_get_meta():
   d = get_meta()
   assert d.get('records') is not None

def test_get_info():
    i = get_info()

    assert isinstance(i, str)
