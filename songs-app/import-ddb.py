# https://medium.com/@ravichauhan03/import-data-from-csv-to-dynamodb-using-aws-sdk-for-python-boto-3-642b25fcfd3d
# Python Script to insert csv records in dynamodb table.
from __future__ import print_function  # Python 2/3 compatibility
from __future__ import division  # Python 2/3 compatiblity for integer division
import argparse
import boto3
from csv import reader
import time
# command line arguments
parser = argparse.ArgumentParser(
    description='Write CSV records to dynamo db table. CSV Header must map to dynamo table field names.')
parser.add_argument('csvFile', help='songs-test.tsv')
parser.add_argument('table', help='Songs')
parser.add_argument('writeRate', default=1, type=string, nargs='?',
                    help='Number of records to write in table per second (default:1)')
parser.add_argument('delimiter', default='|', nargs='?', help='Delimiter for csv records (default=,)')
parser.add_argument('region', default='us-east-1', nargs='?', help='Dynamo db region name (default=us-west-2')
args = parser.parse_args()
print(args)

# dynamodb and table initialization
endpointUrl = "https://dynamodb.us-west-2.amazonaws.com"
dynamodb = boto3.resource('dynamodb', region_name=args.region, endpoint_url=endpointUrl)
table = dynamodb.Table(args.table)

# write records to dynamo db
with open(args.csvFile) as csv_file:
    tokens = reader(csv_file, delimiter=args.delimiter)
    # read first line in file which contains dynamo db field names
    header = next(tokens)
    # read second line in file which contains dynamo db field data types
    headerFormat = next(tokens)
    # rest of file contain new records
    for token in tokens:
        print(token)
        item = {}
        for i, val in enumerate(token):
            print(val)
            if val:
                key = header[i]
                if headerFormat[i] == 'int':
                    val = int(val)
                if headerFormat[i] == 'stringset':
                    tempVal = val.split('|')
                    val = set()
                    for tok in enumerate(tempVal):
                        print(tok)
                        val.add(str(tok[1]))
                print(val)
                item[key] = val
        print(item)
        table.put_item(Item=item)

        time.sleep(1 / args.writeRate)  # to accomodate max write provisioned capacity for table