from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
import jwt
import datetime
from swagger_server.config import config
from flask import make_response, jsonify
# from functools import wraps

# TODO
def check_basicAuth(username, password, required_scopes):
    return {'test_key': 'test_value'}

    # if username and username in ['a', 'b']:
    #     if password and password in ['1', '2', 1, 2]:
    #         # token = jwt.encode(
    #         #     {'user': username,
    #         #      'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=150)}, config.SECRET_KEY)
    #
    #         return {'test_key': 'test_value'}
    #         # return {'token': token.decode('UTF-8')}
    #         # return jsonify({'token': token.decode('UTF-8')})
    #
    # return None
    # return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

    # return {'test_key': 'test_value'}

