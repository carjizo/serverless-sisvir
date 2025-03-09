from typing import List

from domain.usescases.UserUseCases import UserUseCases
from domain.repositories.UserRepository import UserRepository
from domain.models.UserModel import UserModel
from application.validators.UserValidator import UserValidator

class ProductService(UserUseCases):
    
    def __init__(self, user_repository: UserRepository):
        super().__init__(user_repository)

    def all_users(self) -> List[UserModel]:
        return self.user_repository.get_all()

    def user_detail(self, identity_number: str) -> UserModel:
        return self.user_repository.get_by_id(identity_number) 

    def register_user(self, user: UserModel) -> UserModel:
        UserValidator.validate_full_name_empty(user.full_name)
        UserValidator.validate_id_mac_empty(user.id_mac)
        return self.user_repository.add(user)

    def update_product(self, identity_number: int, user: UserModel) -> UserModel:
        UserValidator.validate_full_name_empty(user.full_name)
        UserValidator.validate_id_mac_empty(user.id_mac)
        return self.user_repository.update(identity_number, user)

    def delete_product(self, identity_number: int) -> bool:
        return self.user_repository.delete(identity_number)