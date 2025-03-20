from typing import Protocol, Optional, List
from abc import ABC, abstractclassmethod

from domain.models.UserModel import UserModel
from application.ports.outputs.UserPersistencePort import UserPersistencePort

class UserServicePort(ABC):
    @abstractclassmethod
    def __init__(self, user_persistence_port: UserPersistencePort):
        self.user_persistence_port = user_persistence_port

    @abstractclassmethod
    def find_all(self) -> List[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def find_by_id(self, identity_number: str) -> Optional[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def save(self, user: UserModel) -> UserModel:
        raise NotImplemented

    @abstractclassmethod
    def update(self, identity_number: str, user: UserModel) -> Optional[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def delete_by_id(self, identity_number: str) -> bool:
        raise NotImplemented