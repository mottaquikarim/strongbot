import requests

class Airtable(object):
    
    def __init__(self, api_key=None, base_key=None):
        if api_key is None or base_key is None:
            raise Exception('api_key/base_key not set')

        self.program = 'Regimen'
        self.meta = 'MetaData'

        self.headers = {
            'Authorization': 'Bearer {}'.format(api_key)
        }

        self.base_url = 'https://api.airtable.com'
        self.version = 0
        self.base_key = base_key 

    def get_endpoint(self, endpt):
        url = "{base_url}/v{version}/{base_key}/{endpt}".format(
            base_url=self.base_url,
            version=self.version,
            base_key=self.base_key,
            endpt=endpt
        )

        return url

    def get_tabledata(self, endpt):
        url = self.get_endpoint(endpt=endpt)

        url = "{url}?maxRecords={mr}".format(
            url=url,
            mr=100,
        )
        r = requests.get(
            url,
            headers=self.headers
        )

        return r.json()

    @staticmethod
    def query_data(data, colName, colValue):
        records = data.get('records')
    
        filtered = [r.get('fields', {}).get('Value') for r in records
            if r.get('fields', {}).get(colName) == colValue]

        if len(filtered):
            return filtered[0]

        return None
