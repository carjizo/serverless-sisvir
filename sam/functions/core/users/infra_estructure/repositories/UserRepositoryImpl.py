from typing import Protocol, Optional, List
import json

from domain.repositories.UserRepository import UserRepository
from domain.models.UserModel import UserModel
from timeModel import UserEntity

class UserRepositoryImpl(UserRepository):
    def find_all(self) -> List[UserModel]:
        return []

    def find_by_id(self, identity_number: str) -> Optional[UserModel]:
        userItem = UserEntity.get(identity_number)
        collabJson = json.loads(json.dumps(userItem.to_dict(), default=UserEntity.myconverter))
        user: UserModel = UserModel(
            identity_number=collabJson.get("identityNumber", None),
            full_name=collabJson.get("fullName", None),
            id_mac=collabJson.get("idMac", None),
            id_pathological_history=collabJson.get("idPathologicalHistory", None),
            height=collabJson.get("height", None),
            weight=collabJson.get("weight", None),
            critical_value=collabJson.get("critical_value", None),
            active=collabJson.get("active", False)
        )
        return user

    def add(self, user: UserModel) -> UserModel:
        return {}

    def update(self, identity_number: str, product: UserModel) -> Optional[UserModel]:
        return {}

    def delete_by_id(self, identity_number: str) -> bool:
        return True