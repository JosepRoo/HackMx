import uuid

from app import Database


class Data(object):
    def __init__(self, vehicle, tiempo, leave, icon):
        self.vehicle = vehicle
        self.tiempo = tiempo
        self.leave = leave
        self.icon = icon
    def json(self):
        return {
            'vehicle':self.vehicle,
            'tiempo':self.tiempo,
            'leave':self.leave,
            'icon':self.icon
        }


class Recommendation(object):
    def __init__(self, user_id, fromA, to, data, _id=None):
        self.user_id = user_id
        self.fromA = fromA
        self.to = to
        self.data = [Data(d['vehicle'], d['tiempo'], d['leave'], d['icon']) for d in data]
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_user_id(cls, user_id=None):
        if user_id is None:
            recommendations = Database.find("recommendations", {})
        else:
            recommendations = Database.find("recommendations", {"user_id":user_id})
        return [cls(**recommendation) for recommendation in recommendations]

    def json(self):
        return {
            'user_id': self.user_id,
            'fromA': self.fromA,
            'to': self.to,
            'data': [d.json() for d in self.data],
            '_id': self._id
        }
