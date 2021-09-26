import json
import logging

from lambda_decorators import on_exception
from service.dynamoservices import dynamodb_handler, dynamodb_updates

@on_exception
def log_exception(exception):
    logging.error(exception)
    return get_response_object(500, 'internal_server_error')


def get_response_object(status, result):
    return {
        'statusCode': status,
        "body": result,
        "headers": {'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                    }
    }

@log_exception
def lambda_handler(event, context):
    """
    :param event:
     context:
    """
    if 'queryStringParameters' in event and 'email' in event['queryStringParameters']:
        result = dynamodb_handler(event['queryStringParameters']['email'])
        return get_response_object(200, result)
    elif "body" in event and event["body"]:
        result = dynamodb_updates(json.loads(event["body"]))
        return get_response_object(200, result)
    else:
        return get_response_object(400, 'invalid parameters')
