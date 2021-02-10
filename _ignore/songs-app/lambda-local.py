import boto3
import random
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# the below is from the AWS documentation, needs to be modified for what javascript will want to get back from the Lambda function (all string JSON)
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0: #this check will not be needed, remove the if and make sure both float or int would be turned into str
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

