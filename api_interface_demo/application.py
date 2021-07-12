#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joaquin Rives
@email: joaquin.rives01@gmail.com
@date: Dec 2020
"""

import connexion
from swagger_server import encoder
import os
from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem

# TODO
def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        info = {'sub': 'admin', 'scope': 'secret'}
    elif username == 'foo' and password == 'bar':
        info = {'sub': 'user1', 'scope': ''}
    else:
        # optional: raise exception for custom error response
        return None

    # optional
    if required_scopes is not None and not validate_scope(required_scopes, info['scope']):
        raise OAuthScopeProblem(
                description='Provided user doesn\'t have the required access rights',
                required_scopes=required_scopes,
                token_scopes=info['scope']
            )

    return info


def get_secret(user) -> str:
    return "You are {user} and the secret is 'wbevuec'".format(user=user)


cw = os.getcwd()

# def main():
app = connexion.App(__name__, specification_dir=f"{cw}/swagger_server/swagger/")
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Sitewise Interface API'}, pythonic_params=True)
# application.run()
# application.run(port=8000, debug=True)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

#
#
# # TODO port 5000