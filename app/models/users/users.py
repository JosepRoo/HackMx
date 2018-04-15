import uuid

from flask import session

from app import Database
from app.common.utils import Utils
from app.models.addresses.addresses import Address
from app.models.users.errors import UserErrors
from app.models.vehicles.vehicle import Vehicle


class User(object):

    def __init__(self, name, last_name, email, password, vehicles, weekly_budget, addresses=None, _id=None):
        self.name = name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.vehicles = [Vehicle.create_vehicle(vehicle) for vehicle in vehicles]
        self.weekly_budget = weekly_budget
        self.addresses = [Address.create_address(address) for address in addresses] if addresses is not None else []
        self._id = uuid.uuid4().hex if _id is None else _id

    def get_id(self):
        return self._id
    @staticmethod
    def is_login_valid(email, password):
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            raise UserErrors.UserNotExistsError("Your User doesn't exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your Password was wrong")
        return True

    @staticmethod
    def register_user(name, last_name, email, password, vehicles, weekly_budget, addresses=[]):
        user_data = Database.find_one("users", {"email": email})
        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("the e-mail you used already exists")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does not hace the right format")

        User(name, last_name, email, Utils.hash_password(password), vehicles, weekly_budget, addresses).save_to_db()
        return True

    @classmethod
    def get_users(cls):
        users = Database.find("users", {})
        return [cls(**user) for user in users]

    @classmethod
    def get_users_addresses(cls, user_id=None):
        if user_id is None:
            users = Database.find("users", ({}, {"addresses": 1, "_id": 0}))
        else:
            users = Database.find("users", ({"_id":user_id}, {"addresses": 1, "_id": 0}))
        return [Address.create_address(user['addresses']) for user in users]

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'vehicles': [vehicle.json() for vehicle in self.vehicles],
            'weekly_budget': self.weekly_budget,
            'addresses': [address.json() for address in self.addresses] if self.addresses is not None else [],
            '_id': self._id
        }

    @staticmethod
    def isLogged(email):
        if email is not None:
            return True
        else:
            raise UserErrors.UserNotLoggIn("The User is not Logged in")
