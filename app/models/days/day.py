import datetime
import uuid

from app import Database
from app.models.schedules.schedule import Schedule
from app.models.users.users import User


class Day(object):
    def __init__(self, date, schedules=[], _id=None):
        self.date = datetime.date(date)
        self.schedules = schedules
        self._id = uuid.uuid4().hex if _id is None else _id

    def get_day_schedule_by_id(self, user_id):
        self.schedules = User.get_users_addresses(user_id)
        temp_schedules = Schedule.get_schedules_address(self.date,user_id)
        if temp_schedules is not None:
            for schedule in temp_schedules:
                self.schedules.append(schedule)
        self.schedules.sort(key=lambda x: x.date)

    def get_day_schedule(self):
        for user in User.get_users():
            self.get_day_schedule_by_id(user.get_id())

    def save_to_mongo(self):
        if self.schedules == []:
            self.get_day_schedule()
        Database.insert("days", self.json())

    def json(self):
        return {
            'date':self.date,
            '_id':self._id,
            'schedules': [schedule.json() for schedule in self.schedules]
        }
