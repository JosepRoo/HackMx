from flask import Blueprint, request, session, url_for, render_template, jsonify
from app.common.response import Response
from app.models.users.errors import UserErrors
from app.models.users.users import User


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    try:
        if User.is_login_valid(email, password):
            session['email'] = email
            return jsonify(Response(success=True, records=1, data=email, msg_response="Login Correcto"))
    except UserErrors.UserErrors as e:
        return jsonify(Response(msg_response=e.message))


@user_blueprint.route('/register', methods=['POST'])
def register_user():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    vehicles = request.form['vehicles']
    weekly_budget = request.form['weekly_budget']
    address = request.form['address']
    try:
        if User.register_user(name, last_name, email, password, vehicles, weekly_budget, address):
            session['email'] = email
            return jsonify(Response(success=True, records=1, data=email, msg_response="Registro Exitoso"))
    except UserErrors.UserErrors as e:
        return jsonify(Response(msg_response=e.message))
