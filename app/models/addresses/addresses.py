import uuid

from app import Database
from app.common.utils import Utils
from app.models.addreses.errors import AddressErrors
from app.models.users.errors import UserErrors


class Address(object):

    def __init__(self, name, street, zipCode, state, city, country, period, _id=None):
        self.name = name
        self.street = street
        self.zipCode = zipCode
        self.state = state
        self.city = city
        self.country = country
        self.period = period
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_user_addresses(cls, email):
        addresses_data = Database.find("users", {"email": email}, {"addresses": 1, "_id": 0 })
        if addresses_data is None:
            raise UserErrors.UserNotExistsError("Your User doesn't exist")
        if addresses_data["addresses"] is None:
            raise AddressErrors.UserHasNoAddresses("User does not have any register addresses")
        return [cls(**address) for address in addresses_data]
