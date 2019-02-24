from flask import Blueprint
from flask import jsonify


api = Blueprint('api_v1', __name__)


# Import any endpoints here to make them available
#from . import dis_endpoint, dat_endpoint

@api.route('/checkin')
def hello_world():
    d = {
        "lattitude" : -96.754,
        "longitude" : 32.99,
        "user_id" : 10001
    }
    return jsonify(d)