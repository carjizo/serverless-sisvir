from typing import Protocol, Optional, List
from abc import ABC, abstractclassmethod

from domain.models.UserModel import UserModel

class UserRepository(ABC):
    @abstractclassmethod
    def get_all(self) -> List[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def get_by_id(self, identity_number: str) -> Optional[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def add(self, user: UserModel) -> UserModel:
        raise NotImplemented

    @abstractclassmethod
    def update(self, identity_number: str, product: UserModel) -> Optional[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def delete(self, identity_number: str) -> bool:
        raise NotImplemented