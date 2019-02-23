from flask import Blueprint


api = Blueprint('api_v1', __name__)


# Import any endpoints here to make them available
#from . import dis_endpoint, dat_endpoint

@api.route('/test')
def hello_world():
    return 'Hello, World!'