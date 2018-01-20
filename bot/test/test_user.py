from bot.models.user import User, fmt_time
from datetime import datetime
import unittest

class TestUser(unittest.TestCase):
    def test_init(self):
        test_user = User()

        assert test_user.dynamodb is not None
        assert test_user.table is not None

    def test_create_row(self):
        test_user = User()

        now = datetime.now()
        u = test_user.create_row(phonenumber='XXX', fmt_time=now.strftime('%Y-%m-%d %H:%M'))

        rows = test_user.search_by_number(phonenumber='XXX')
        assert rows is not None
        assert len(rows) > 0

        u = test_user.create_row()
        assert u is None

    def test_search_by_number(self):
        test_user = User()

        u = test_user.search_by_number()
        assert len(u) == 0

        u = test_user.search_by_number(phonenumber='XXXXXX')
        assert len(u) == 0
