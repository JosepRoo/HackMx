import uuid

import datetime

from app import Database
from app.models.addresses.addresses import Address
from app.models.users.users import User


class Schedule(object):
    def __init__(self, user_id, description, address, date, _id=None):
        self.user_id = user_id
        self.description = description
        self.address = Address.create_address(address)
        self.date = datetime.datetime.strptime(date, "%Y/%m%d")
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_schedules(cls, date=None, user_id=None):
        if user_id is None:
            if date is None:
                schedules = Database.find("schedules", {})
            else:
                schedules = Database.find("schedules", {"$date": date})
        else:
            schedules = Database.find("schedules", {"$date": date, "user_id":user_id})
        return [cls(**schedule) for schedule in schedules]

    @classmethod
    def get_schedules_address(cls, date=None, user_id=None):
        if user_id is None:
            if date is None:
                schedules = Database.find("schedules", ({}, {"address": 1, "_id": 0}))
            else:
                schedules = Database.find("schedules", ({"$date": date}, {"address": 1, "_id": 0}))
        else:
            schedules = Database.find("schedules", ({"$date": date, "user_id": user_id}, {"address": 1, "_id": 0}))
        return [Address.create_address(schedule[['address']]) for schedule in schedules]

    @staticmethod
    def create_schedules_from_address():
        users = User.get_users()
        schedules = []
        for user in users:
            for address in user.addresses:
                schedules.append(Schedule(user.get_id(), "Horario Fijo", address))
        return schedules

    def save_to_json(self):
        Database.insert("schedules", self.json())

    def json(self):
        return {
            'user_id': self.user_id,
            'description': self.description,
            'address': self.address.json(),
            'date': self.date.strftime("%Y/%m/%d"),
            '_id': self._id
        }
