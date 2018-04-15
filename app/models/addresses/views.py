from flask import Blueprint, request, session, url_for, render_template, jsonify
from app.common.response import Response
from app.models.users.errors import UserErrors
from app.models.users.users import User
from app.models.addresses.addresses import Address


user_blueprint = Blueprint('addresses', __name__)


@user_blueprint.route('/getUserAddresses', methods=['POST'])

def get_user_addresses():
    email = session['email']
    try:
        if Address.get_user_addresses(email):
            session['email'] = email
            return jsonify(Response(success=True, records=1, data=email, msg_response="Login Correcto"))
    except AddressErrors.AddressErrors as e:
        return jsonify(Response(msg_response=e.message))


@user_blueprint.route('/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    try:
        if User.register_user(email, password):
            session['email'] = email
            return jsonify(Response(success=True, records=1, data=email, msg_response="Registro Exitoso"))
    except UserErrors.UserErrors as e:
        return jsonify(Response(msg_response=e.message))
