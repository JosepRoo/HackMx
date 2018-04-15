import uuid
from app import Database
from app.models.addresses.errors import AddressErrors
from app.models.users.errors import UserErrors


class Address(object):
    def __init__(self, name, street, zip_code, state, city, country, period, _id=None):
        self.name = name
        self.street = street
        self.zip_code = zip_code
        self.state = state
        self.city = city
        self.country = country
        self.period = period
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_user_addresses(cls, email):
        addresses_data = Database.find("users", ({"email": email}, {"addresses": 1, "_id": 0}))
        if addresses_data is None:
            raise UserErrors.UserNotExistsError("Your User doesn't exist")
        if addresses_data["addresses"] is None:
            raise AddressErrors.UserHasNoAddresses("User does not have any register addresses")
        return [cls(**address) for address in addresses_data]

    @classmethod
    def create_address(cls, address):
        return cls(**address)

    def update_mongo(self, user_email):
        Database.update_one("users", {"$push": self.json()}, {"email": user_email})

    def save_to_mongo(self):
        Database.insert("Addresses", self.json())

    def json(self):
        return{
            'name': self.name,
            'street': self.street,
            'zip_code': self.zip_code,
            'state': self.state,
            'city': self.city,
            'country': self.country,
            'period': self.period,
            '_id': self._id
        }

