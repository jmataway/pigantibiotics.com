import boto3
import random
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

firstId = 1
lastId = 3

dynamodb = boto3.resource("dynamodb", region_name='us-east-1')

table = dynamodb.Table('Songs')

id = random.randint(firstId,lastId)

try:
    response = table.get_item(
        Key={
            'ID': id,
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("Song retrieval succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))

""" item = response['Item']
print(item)
print(type(item)) """

"""above works to pull a specific item. What needs to happen:
3. Improve the above boto3 and ddb code, using: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html as a starting guide
4. Pull the various key values from the "response" item (so pull the song name, artist, year, etc from the returned dictionary) and format better
"""