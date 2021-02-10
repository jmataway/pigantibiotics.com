import boto3
import random
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
                return str(o)
        return super(DecimalEncoder, self).default(o)

def getRandomSong(event, context):
    firstId = 1
    lastId = 3
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table('Songs')
    id = random.randint(firstId,lastId)
    response = table.get_item(
        Key={
            'ID': id,
        }
    )
    item = response['Item']
    jitem = json.dumps(item, indent=4, cls=DecimalEncoder)
    return jitem
