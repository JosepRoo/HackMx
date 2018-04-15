import uuid

from app import Database


class Data(object):
    def __init__(self, vehicle,tiempo , leave):
        self.vehicle = vehicle
        self.tiempo = tiempo
        self.leave = leave

    def json(self):
        return {
            'vehicle':self.vehicle,
            'tiempo':self.tiempo,
            'leave':self.leave
        }


class Recommendation(object):
    def __init__(self, user_id, fromA, to, data, _id=None):
        self.user_id = user_id
        self.fromA = fromA
        self.to = to
        self.data = Data(data['vehicle'], data['tiempo'], data['leave'])
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
            'data': self.data.json(),
            '_id' : self._id
        }
