from flask import Blueprint, request, session, jsonify
from app.common.response import Response
from app.models.vehicles.vehicle import Vehicle

vehicle_blueprint = Blueprint('vehicles', __name__)

@vehicle_blueprint.route('/get')
@vehicle_blueprint.route('/get/<string:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id=None):
    vehicles = None
    if vehicle_id is None:
        vehicles = [vehicle.json() for vehicle in Vehicle.get_vehicles()]
    else:
        vehicles = Vehicle.get_vehicle(vehicle_id).json()
    return jsonify(Response(success=True, records=len(vehicles), data=vehicles).json())
