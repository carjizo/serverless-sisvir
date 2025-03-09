import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
environment = os.environ

def lambda_handler(event, _):
    logger.info(f"event: {event}")
    logger.info(f"environment: {environment}")
    print(event)
    method = event['httpMethod']
    path = event['requestContext']['resourcePath']