import json

from application.services.UserService import UserService
from infraestructure.repositories.UserRepositoryImpl import UserRepositoryImpl
from infraestructure.routers.UserPath import UserPath

class UserRouter:
    def __init__(self, event):
        self.event = event
        self.method = self.event['httpMethod']
        self.path = self.event['requestContext']['resourcePath']
        self.body = {} if self.event.get('body') is None else json.loads(self.event.get('body'))

        user_repository_impl :UserRepositoryImpl = UserRepositoryImpl()
        self.user_service: UserService = UserService(user_repository_impl)

    def route(self):
        if self.method == "GET" and UserPath.GET_USER_BY_ID.match(self.path):
            identityNumber = self.event['pathParameters']['identityNumber']
            self.find_by_id(identityNumber)
        else:
            return self.method_not_allowed()

    def create_user(self, body: dict):
        return self.response(201, {})

    def find_by_id(self, identityNumber: str):
        if not identityNumber:
            return self.response(400, {"error": "User ID is required"})
        user = self.user_service.user_detail(identityNumber)
        if user:
            return self.response(200, user)
        else:
            return self.response(404, {"error": "User not found"})

    def method_not_allowed(self):
        return self.response(405, {"error": "Method not allowed"})

    @staticmethod
    def response(status_code, body):
        return {
            "statusCode": status_code,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps(body)
        }