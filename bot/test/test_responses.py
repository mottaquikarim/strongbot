from bot.responses import hello_new_user, \
    start_workout, \
    send_more_info, \
    error_msg

def test_hello_new_user():
    r = hello_new_user()

    str_r = str(r)
    assert str_r.startswith('<?xml version="1.0" encoding="UTF-8"?><Response><Message>')
    assert str_r.endswith('</Message></Response>')

def test_start_workout():
    r = start_workout()

    str_r = str(r)
    assert str_r.startswith('<?xml version="1.0" encoding="UTF-8"?><Response><Message>')
    assert str_r.endswith('</Message></Response>')

def test_send_more_info():
    r = send_more_info('test')

    str_r = str(r)
    assert str_r.startswith('<?xml version="1.0" encoding="UTF-8"?><Response><Message>')
    assert str_r.endswith('</Message></Response>')

def test_error_msg():
    r = error_msg()

    str_r = str(r)
    assert str_r.startswith('<?xml version="1.0" encoding="UTF-8"?><Response><Message>')
    assert str_r.endswith('</Message></Response>')
