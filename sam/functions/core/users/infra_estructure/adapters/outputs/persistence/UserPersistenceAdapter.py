from typing import Protocol, Optional, List
import json

from domain.repositories.UserRepository import UserRepository
from domain.models.UserModel import UserModel
from application.ports.outputs.UserPersistencePort import UserPersistencePort
from timeModel import UserEntity
from domain.models.UserModel import UserModel, UserModelBuilder

class UserPersistenceAdapter(UserPersistencePort):

    def find_all(self) -> List[UserModel]:
        return []

    def find_by_id(self, identity_number: str) -> Optional[UserModel]:
        user_dynamodb = UserEntity.get(identity_number)
        user_json = json.loads(json.dumps(user_dynamodb.to_dict(), default=UserEntity.myconverter))

        return (UserModelBuilder()
                        .identity_number(user_json.get("identityNumber", None))
                        .full_name(user_json.get("fullName", None))
                        .id_mac(user_json.get("idMac", None))
                        .id_pathological_history(user_json.get("idPathologicalHistory", None))
                        .height(user_json.get("height", None))
                        .weight(user_json.get("weight", None))
                        .critical_value(user_json.get("critical_value", None))
                        .active(user_json.get("active", False))
                        .build())

    def save(self, user: UserModel) -> UserModel:
        return {}


    def delete_by_id(self, identity_number: str) -> bool:
        return True