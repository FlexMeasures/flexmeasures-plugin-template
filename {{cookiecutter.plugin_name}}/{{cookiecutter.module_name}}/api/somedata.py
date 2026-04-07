from flask_security import auth_token_required
from flask_json import as_json

from .. import {{cookiecutter.module_name}}_api_bp


@{{cookiecutter.module_name}}_api_bp.route("/somedata")
@auth_token_required
@as_json
def somedata():
    """
    ---
    get:
      summary: Get some data
      description: |
        Endpoint to get some data

      security:
        - ApiKeyAuth: []
      responses:
        200:
          description: PROCESSED
        400:
          description: INVALID_REQUEST
        401:
          description: UNAUTHORIZED
        403:
          description: INVALID_SENDER
        422:
          description: UNPROCESSABLE_ENTITY
      tags:
        - {{cookiecutter.plugin_name}}
    """
    return dict(a=1, b=2)
