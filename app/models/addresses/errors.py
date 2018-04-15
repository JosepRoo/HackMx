class AddressErrors(Exception):
    def __init__(self, message):
        self.message = message


class AddressNotExistsError(AddressErrors):
    pass


class IncorrectPasswordError(AddressErrors):
    pass


class AddressAlreadyRegisteredError(AddressErrors):
    pass

class UserHasNoAddresses(AddressErrors):
    pass
