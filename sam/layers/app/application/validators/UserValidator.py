from domain.exceptions.UserException import FullNameIsEmpty, IdMacIsEmpty

class UserValidator:

    @staticmethod
    def validate_full_name_empty(full_name: str) -> float:
        if full_name is None or full_name == "":
            raise FullNameIsEmpty

    @staticmethod
    def validate_id_mac_empty(id_mac: str) -> None:
        if id_mac is None or id_mac == "":
            raise IdMacIsEmpty