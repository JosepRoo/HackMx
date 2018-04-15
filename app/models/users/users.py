import uuid

from app import Database
from app.common.utils import Utils
from app.models.users.errors import UserErrors
from app.models.vehicles.vehicle import Vehicle


class User(object):

    def __init__(self, name, last_name, email, password, vehicles, weekly_budget, addresses, _id=None):
        self.name = name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.vehicles = [Vehicle.create_vehicle(vehicle) for vehicle in vehicles]
        self.weekly_budget = weekly_budget
        self.addresses = addresses
        self._id = uuid.uuid4().hex if _id is None else _id

    @staticmethod
    def is_login_valid(email, password):
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            raise UserErrors.UserNotExistsError("Your User doesn't exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your Password was wrong")
        return True

    @staticmethod
    def register_user(name, last_name, email, password, vehicles, weekly_budget, addresses):
        user_data = Database.find_one("users", {"email": email})
        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("the e-mail you used already exists")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does not hace the right format")

        User(name, last_name, email, Utils.hash_password(password), vehicles, weekly_budget, addresses).save_to_db()
        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'vehicles': self.vehicles,
            'weekly_budget': self.weekly_budget,
            'addresses': self.addresses,
            '_id': self._id
        }
