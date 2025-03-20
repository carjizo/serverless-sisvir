import json

from infra_estructure.adapters.inputs.rest.UserRestAdapter import UserRestAdapter
from infra_estructure.adapters.inputs.rest.routers.UserPath import UserPath

class UserRouter:
    def __init__(self, event):
        self.event = event
        self.method = self.event['httpMethod']
        self.path = self.event['requestContext']['resourcePath']
        self.body = {} if self.event.get('body') is None else json.loads(self.event.get('body'))
        self.user_rest_adapter: UserRestAdapter = UserRestAdapter()

    def route(self) -> dict:
        if self.method == "GET" and UserPath.GET_USER_BY_ID.match(self.path):
            identity_number = self.event['pathParameters']['identityNumber']
            rsp = self.user_rest_adapter.find_by_id(identity_number)
        else:
            rsp = self.user_rest_adapter.api_response.method_not_allowed()
        return  rsp

