import uuid
from app import Database
from app.models.addresses.errors import AddressErrors
from app.models.period.period import Period
from app.models.users.errors import UserErrors


class Address(object):
    def __init__(self, name, coord, period, _id=None):
        self.name = name
        self.coord = coord
        self.period = Period.create_period(period)
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
            'coord': self.coord,
            'period': self.period.json(),
            '_id': self._id
        }

print(Address("Casa",[19.54720747671817, -99.29932693374141],{'day': 'Monday', 'initialTime': '06:00', 'finalTime': '07:00'}).json())
print(Address("Trabajo",[119.4427747,-99.2171993],{'day': 'Monday', 'initialTime': '09:00', 'finalTime': '15:00'}).json())
print(Address("Escuela",[19.5949154,-99.2298629],{'day': 'Monday', 'initialTime': '16:00', 'finalTime': '22:00'}).json())
print(Address("Casa",[19.54720747671817, -99.29932693374141],{'day': 'Monday', 'initialTime': '22:50', 'finalTime': '23:00'}).json())
