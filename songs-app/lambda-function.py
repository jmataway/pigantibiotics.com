import boto3
import random
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

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
    return item
