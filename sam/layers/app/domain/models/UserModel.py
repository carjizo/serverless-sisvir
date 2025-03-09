from domain.exceptions.UserException import FullNameIsEmpty, IdMacIsEmpty

class UserModel:
    def __init__(self, identity_number: str, full_name: str, id_mac: str, id_pathological_history: str,
                height: int, weight: int, critical_value: int , active: bool):
        self.__validate_full_name(full_name)
        self.__validate_id_mac(id_mac)

        self.identity_number: str = identity_number
        self.full_name: str = full_name
        self.id_mac: str = id_mac
        self.id_pathological_history: str = id_pathological_history
        self.height: int = height
        self.weight: int = weight
        self.critical_value: int = critical_value
        self.active: bool = active

    @staticmethod
    def __validate_full_name(full_name: str):
        if full_name is None or full_name == "":
            raise FullNameIsEmpty

    @staticmethod
    def __validate_id_mac(id_mac: str):
        if id_mac is None or id_mac == "":
            raise IdMacIsEmpty