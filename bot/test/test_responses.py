from bot.responses import hello_new_user

def test_hello_new_user():
    r = hello_new_user()

    str_r = str(r)
    assert str_r.startswith('<?xml version="1.0" encoding="UTF-8"?><Response><Message>')
    assert str_r.endswith('</Message></Response>')
