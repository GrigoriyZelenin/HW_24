from flask import Blueprint, request, jsonify

from bulider import build_query
from models import BatchRequestParams

main_bp = Blueprint("main", __name__)


@main_bp.route('/perform_query', methods=["POST"])
def perform_query():

    try:
        params = BatchRequestParams().load(request.json)
    except ValueError as e:
        return e, 400

    result = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            param=query['value'],
            data=result )

    return jsonify(result)

