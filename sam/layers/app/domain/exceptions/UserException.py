class FullNameIsEmpty(Exception):
    def __init__(self):
        super().__init__('The full_name es empty')

class IdMacIsEmpty(Exception):
    def __init__(self):
        super().__init__('The id_mac es empty')