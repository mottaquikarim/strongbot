import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

def fmt_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M')

class User(object):
    def __init__(self, name='Users'):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(name)

    def create_row(self, phonenumber=None, fmt_time=fmt_time()):
        if not phonenumber:
            return None

        resp = self.table.put_item(
            Item={
                'PhoneNumber': phonenumber,
                'Timestamp': fmt_time
            }
        )

        return resp 

    def search_by_number(self, phonenumber=None):
        if not phonenumber:
            return []

        resp = self.table.query(
            KeyConditionExpression=Key('PhoneNumber').eq(phonenumber)
        )

        return resp.get('Items', [])
