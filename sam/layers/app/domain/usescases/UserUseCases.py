from abc import ABC, abstractclassmethod
from typing import List

from domain.models.UserModel import UserModel
from domain.repositories.UserRepository import UserRepository


class UserUseCases(ABC):

    @abstractclassmethod
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    @abstractclassmethod
    def find_all(self) -> List[UserModel]:
        raise NotImplemented

    @abstractclassmethod
    def find_by_id(self, identity_number: str) -> UserModel:
        raise NotImplemented

    @abstractclassmethod
    def save(self, user: UserModel) -> UserModel:
        raise NotImplemented

    @abstractclassmethod
    def update(self, identity_number: int, user: UserModel) -> UserModel:
        raise NotImplemented

    @abstractclassmethod
    def delete_by_id(self, identity_number: int) -> bool:
        raise NotImplemented