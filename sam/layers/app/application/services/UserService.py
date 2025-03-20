from typing import List, Optional

# from domain.usescases.UserUseCases import UserUseCases
# from domain.repositories.UserRepository import UserRepository
from domain.models.UserModel import UserModel, UserModelBuilder
# from application.validators.UserValidator import UserValidator
from application.ports.inputs.UserServicePort import UserServicePort
from application.ports.outputs.UserPersistencePort import UserPersistencePort


class UserService(UserServicePort):

    def __init__(self, user_persistence_port: UserPersistencePort):
        super().__init__(user_persistence_port)

    def find_all(self) -> List[UserModel]:
        return self.user_persistence_port.find_all()

    def find_by_id(self, identity_number: str) -> Optional[UserModel]:
        return self.user_persistence_port.find_by_id(identity_number)

    def save(self, user: UserModel) -> UserModel:
        # UserValidator.validate_full_name_empty(user.full_name)
        # UserValidator.validate_id_mac_empty(user.id_mac)
        return self.user_persistence_port.add(user)

    def update(self, identity_number: str, user: UserModel) -> Optional[UserModel]:
        # UserValidator.validate_full_name_empty(user.full_name)
        # UserValidator.validate_id_mac_empty(user.id_mac)
        user_db: Optional[UserModel] = self.user_persistence_port.find_by_id(identity_number)
        updated_user = (UserModelBuilder(user_db)
                        .identity_number(user.identity_number)
                        .full_name(user.full_name)
                        .id_mac(user.id_mac)
                        .id_pathological_history(user.id_pathological_history)
                        .height(user.height)
                        .weight(user.weight)
                        .critical_value(user.critical_value)
                        .active(user.active)
                        .build())
        return self.user_persistence_port.add(updated_user)

    def delete_by_id(self, identity_number: str) -> bool:
        return self.user_persistence_port.delete_by_id(identity_number)