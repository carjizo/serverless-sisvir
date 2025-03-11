import logging
import os

from infraestructure.routers.UserRouter import UserRouter

logger = logging.getLogger()
logger.setLevel(logging.INFO)
environment = os.environ

def lambda_handler(event, _):
    logger.info(f"event: {event}")
    logger.info(f"environment: {environment}")
    print("event", event)
    api_router = UserRouter(event)
    print("444444")
    api_router.route()