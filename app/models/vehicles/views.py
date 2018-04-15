from flask import Blueprint, request, session, jsonify
from app.common.response import Response
from app.models.users.errors import UserErrors
from app.models.vehicles.vehicle import Vehicle

user_blueprint = Blueprint('vehicles', __name__)

@user_blueprint.route('/get_hecile/<string:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id=None):
    vehicles = None
    if vehicle_id == None:
        vehicles = Vehicle.get_vehicles()
    else:
        vehicles = Vehicle.get_vehicle(vehicle_id)
    return jsonify(Response(success=True, records=len(vehicle_id), data=vehicles))
