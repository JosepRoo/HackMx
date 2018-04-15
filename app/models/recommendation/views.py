from flask import Blueprint, request, session, jsonify
from app.common.response import Response
from app.models.recommendation.recommendation import Recommendation

recommendations_blueprint = Blueprint('recommendations', __name__)

@recommendations_blueprint.route('/get', methods=['GET'])
@recommendations_blueprint.route('/get/<string:user_id>', methods=['GET'])
def get_by_id(user_id=None):
    data = Recommendation.get_by_user_id(user_id)
    if data is not None:
        return jsonify(Response(success=True, records=len(data), data=[d.json() for d in data]).json())
    else:
        return jsonify(Response(msg_response="no data for the request"))
