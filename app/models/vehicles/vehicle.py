import uuid

from app import Database


class Vehicle(object):
    def __init__(self, name, icon, cost, description, maxDistance, _id=None):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.description = description
        self.maxDistance = maxDistance
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_vehicles(cls):
        vehicles = Database.find("vehicles", {})
        return [cls(**vehicle) for vehicle in vehicles]

    @classmethod
    def get_vehicle(cls, _id):
        vehicle_data = Database.find_one("vehicles", {"_id":_id})
        return cls(**vehicle_data)

    @classmethod
    def create_vehicle(cls, vehicle):
        return cls(**vehicle)

    def save_to_db(self):
        Database.insert("vehicles", self.json())

    def json(self):
        return {
            'name': self.name,
            'icon': self.icon,
            'cost': self.cost,
            'description': self.description,
            'maxDistance': self.maxDistance,
            '_id': self._id
        }
