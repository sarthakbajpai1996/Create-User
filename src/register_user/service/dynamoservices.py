import boto3
import os
import json

from boto3.dynamodb.conditions import Key


def write_in_dynamo(data):
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.put_item(
        TableName=os.environ['USER_TABLE'],
        Item=data
    )
    print(response)

def query_dynamo(telephone_number):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['USER_TABLE'])
    response = table.query(
        KeyConditionExpression=Key('telephone_number').eq(telephone_number)
    )

    if len(response['Items']):
        return json.dumps(response['Items'])
    return False

def dynamodb_handler(email):
    data = query_dynamo(email)
    if data:
        return data
    else:
        return("User does not exists")

def dynamodb_updates(data):
    if 'telephone_number' in data and data['telephone_number'] and data["phone_password"]:
        write_in_dynamo({"telephone_number":data['telephone_number'],'phone_password':data["phone_password"]})
        return "User Updated"
    else:
        return "Telephone Number missing"

