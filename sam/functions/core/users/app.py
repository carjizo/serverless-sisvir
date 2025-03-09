import logging
import os
import json

from domain.models.UserModel import UserModel

logger = logging.getLogger()
logger.setLevel(logging.INFO)
environment = os.environ

def lambda_handler(event, _):
    logger.info(f"event: {event}")
    logger.info(f"environment: {environment}")
    method = event['httpMethod']
    path = event['requestContext']['resourcePath']
    
    body = {} if event.get('body') is None else json.loads(event.get('body'))
    print('#body', body)
    print('#path', path)
    print("d")
    
    try:        
        # if method == 'POST' and Constante.ADD_ANALYST.match(path):
        #     status_code, response = service.insertAnalyst(body)
        # else:
        #     print('No se encuentro path')
        status_code, response = 200, {}
        return {
            "statusCode": status_code,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*" 
            },
            "body": "oka",
        }
    except Exception as e:
        print("Exception >> error: {} ".format(e))
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body":  json.dumps(e)
        }