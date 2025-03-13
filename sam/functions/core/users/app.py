import logging
import os

from infra_estructure.routers.UserRouter import UserRouter

logger = logging.getLogger()
logger.setLevel(logging.INFO)
environment = os.environ

def lambda_handler(event, _):
    logger.info(f"event: {event}")
    logger.info(f"environment: {environment}")
    api_router = UserRouter(event)
    return  api_router.route()