from application.services.UserService import UserService
from infra_estructure.repositories.UserRepositoryImpl import UserRepositoryImpl
from infraestructure.apiresponse.ApiResponse import ApiResponse

class UserController:
    def __init__(self):
        self.api_response: ApiResponse = ApiResponse()
        user_repository_impl: UserRepositoryImpl = UserRepositoryImpl()
        self.user_service: UserService = UserService(user_repository_impl)

    def create_user(self, body: dict) -> dict:
        return self.api_response.response(201, {})

    def find_by_id(self, identity_number: str) -> dict:
        if not identity_number:
            return self.api_response.response(400, {"error": "User ID is required"})
        user = self.user_service.user_detail(identity_number)
        if user:
            return self.api_response.response(200, {"status": "oka"})
        else:
            return self.api_response.response(404, {"error": "User not found"})