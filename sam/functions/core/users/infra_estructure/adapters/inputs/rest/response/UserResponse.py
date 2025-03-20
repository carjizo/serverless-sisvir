from typing import Optional

class UserResponse:
    def __init__(self,
                identity_number: Optional[str] = None,
                full_name: Optional[str] = None,
                id_mac: Optional[str] = None,
                id_pathological_history: Optional[str] = None,
                height: Optional[int] = None,
                weight: Optional[int] = None,
                critical_value: Optional[int] = None ,
                active: Optional[int] = True):

        self._identity_number = identity_number
        self._full_name = full_name
        self._id_mac = id_mac
        self._id_pathological_history = id_pathological_history
        self._height = height
        self._weight = weight
        self._critical_value = critical_value
        self._active = active

    # Getters and Setters
    @property
    def identity_number(self):
        return self._identity_number

    @identity_number.setter
    def identity_number(self, value):
        self._identity_number = value

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def id_mac(self):
        return self._id_mac

    @id_mac.setter
    def id_mac(self, value):
        self._id_mac = value

    @property
    def id_pathological_history(self):
        return self._id_pathological_history

    @id_pathological_history.setter
    def id_pathological_history(self, value):
        self._id_pathological_history = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def critical_value(self):
        return self._critical_value

    @critical_value.setter
    def critical_value(self, value):
        self._critical_value = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

class UserModelBuilder:
    def __init__(self):
        self._identity_number: Optional[str] = None
        self._full_name: Optional[str] = None
        self._id_mac: Optional[str] = None
        self._id_pathological_history: Optional[str] = None
        self._height: Optional[int] = None
        self._weight: Optional[int] = None
        self._critical_value: Optional[int] = None
        self._active: Optional[int] = True

    def identity_number(self, identity_number: str) -> 'UserModelBuilder':
        self._identity_number = identity_number
        return self

    def full_name(self, full_name: str) -> 'UserModelBuilder':
        self._full_name = full_name
        return self

    def id_mac(self, id_mac: str) -> 'UserModelBuilder':
        self._id_mac = id_mac
        return self

    def id_pathological_history(self, id_pathological_history: str) -> 'UserModelBuilder':
        self._id_pathological_history = id_pathological_history
        return self

    def height(self, height: int) -> 'UserModelBuilder':
        self._height = height
        return self

    def weight(self, weight: int) -> 'UserModelBuilder':
        self._weight = weight
        return self

    def critical_value(self, critical_value: int) -> 'UserModelBuilder':
        self._critical_value = critical_value
        return self

    def active(self, active: bool) -> 'UserModelBuilder':
        self._active = active
        return self

    def build(self) -> UserResponse:
        return UserResponse(self._identity_number,
                        self._full_name,
                        self._id_mac,
                        self._id_pathological_history,
                        self._height,
                        self._weight,
                        self._critical_value,
                        self._active)