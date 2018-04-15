from flask import Blueprint, request, session, jsonify
from app.common.response import Response
from app.models.addresses.addresses import Address
from app.models.users.errors import UserErrors
from app.models.users.users import User
from app.models.addresses.errors import AddressErrors


address_blueprint = Blueprint('addresses', __name__)


@address_blueprint.route('/get_user_addresses', methods=['GET'])
def get_user_addresses():
    email = session['email']

    try:
        if User.isLogged(email):
            addresses = [address.json() for address in Address.get_user_addresses(email)]
            if addresses is not None:
                return jsonify(Response(success=True, records=len(addresses), data=addresses, msg_response="Login Correcto").json())
    except AddressErrors as e:
        return jsonify(Response(msg_response=e.message))
    except UserErrors as e:
        return jsonify(Response(msg_response=e.message))

@address_blueprint.route('/add_address', methods=['PUT'])
def add_address():
    email = session['email']
    try:
        if User.isLogged(email):
            Address.update_mongo(email)
    except:
        return jsonify(Response(msg_response=e.message))
