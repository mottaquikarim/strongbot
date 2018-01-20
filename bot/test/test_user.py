from bot.models.user import User, fmt_time
from datetime import datetime
import unittest
from unittest.mock import patch

class TestUser(unittest.TestCase):
    @patch('boto3.resource')
    def test_init(self, Boto3Resource):
        test_user = User()
        Boto3Resource.assert_called()

    @patch('boto3.resource')
    def test_create_row(self, Boto3Resource):
        #Boto3Resource.Table.put_item.return_value = True

        test_user = User()

        test_user.table.put_item.side_effect = lambda *a, **kw: 'MOCKED' 

        now = datetime.now()
        u = test_user.create_row(phonenumber='XXX', fmt_time=now.strftime('%Y-%m-%d %H:%M'))

        assert u == 'MOCKED'
        test_user.table.put_item.assert_called_once()

        u = test_user.create_row()
        assert u is None

    @patch('boto3.resource')
    def test_search_by_number(self, Boto3Resource):
        test_user = User()
        test_user.table.query.side_effect = lambda *a, **kw: {
            'Items': ['MOCKED']
        }

        u = test_user.search_by_number()
        assert u == [] 

        u = test_user.search_by_number(phonenumber='XXXXXX')
        assert u == ['MOCKED']
        test_user.table.query.assert_called_once()
