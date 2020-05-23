import boto3
import random

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
print(item)
print(type(item))

"""above works to pull a specific item. What needs to happen:
3. Improve the above boto3 and ddb code, using: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html as a starting guide
4. Pull the various key values from the "response" item (so pull the song name, artist, year, etc from the returned dictionary) and format better
"""