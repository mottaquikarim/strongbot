from bot.models.airtable import Airtable 
import pytest
import os
import unittest


class TestAirtable(unittest.TestCase):
    def test_init(self):
        with pytest.raises(Exception) as e_info:
            test_table = Airtable()
    
        test_table = Airtable(
            api_key='API_KEY',
            base_key='BASE_KEY',
        )

        assert test_table.program == 'Regimen'

    def test_get_endpoint(self):
        test_table = Airtable(
            api_key='API_KEY',
            base_key='BASE_KEY',
        )

        url = test_table.get_endpoint(
            endpt=test_table.program,
        )
        print(url)

        assert url == 'https://api.airtable.com/v0/BASE_KEY/Regimen'

    def test_get_program(self):
        import bot.config
        if os.environ.get('AIRTABLE_API_KEY'):
            api_key = os.environ.get('AIRTABLE_API_KEY')
        else:
            api_key = bot.config.AIRTABLE_API_KEY

        if os.environ.get('AIRTABLE_BASE_KEY'):
            base_key = os.environ.get('AIRTABLE_BASE_KEY')
        else:
            base_key = bot.config.AIRTABLE_BASE_KEY

        test_table = Airtable(
            api_key=api_key,
            base_key=base_key,
        )

        program = test_table.get_tabledata(endpt=test_table.program)

        assert program.get('records') is not None

    def test_query_data(self):
        import bot.config
        api_key = bot.config.AIRTABLE_API_KEY
        base_key = bot.config.AIRTABLE_BASE_KEY

        test_table = Airtable(
            api_key=api_key,
            base_key=base_key,
        )

        meta = test_table.get_tabledata(endpt=test_table.meta)

        d = Airtable.query_data(meta, 'Name', 'About')
        assert isinstance(d, str)

        d = Airtable.query_data(meta, 'Name', 'DNE')
        assert d is None
