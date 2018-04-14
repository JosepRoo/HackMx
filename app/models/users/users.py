import uuid

from app import Database
from app.common.utils import Utils
from app.models.users.errors import UserErrors


class User(object):

    def __init__(self, name, last_name, email, password, vehicles, weekly_budget, address, _id=None):
        self.name = name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.vehicles = vehicles
        self.weekly_budget = weekly_budget
        self.address = address
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
    def register_user(name, last_name, email, password, vehicles, weekly_budget, address):
        user_data = Database.find_one("users", {"email": email})
        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("the e-mail you used already exists")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does not hace the right format")

        User(name, last_name, email, Utils.hash_password(password), vehicles, weekly_budget, address).save_to_db()
        return True


    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
