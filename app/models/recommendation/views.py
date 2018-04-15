from flask import Blueprint, request, session, jsonify
from app.common.response import Response
from app.models.recommendation.recommendation import Recommendation

recommendations_blueprint = Blueprint('recommendations', __name__)

@recommendations_blueprint.route('/get/<string:user_id>', methods=['GET'])
def get_by_id(user_id):
    data = Recommendation.get_by_user_id(user_id)
    if data is not None:
        return jsonify(Response(success=True, records=len(data), data=data))
    else:
        return jsonify(Response(msg_response="no data for the request"))
