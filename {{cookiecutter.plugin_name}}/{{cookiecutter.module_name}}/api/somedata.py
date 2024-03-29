from flask_security import auth_token_required
from flask_json import as_json

from .. import {{cookiecutter.module_name}}_api_bp


@{{cookiecutter.module_name}}_api_bp.route("/somedata")
@auth_token_required
@as_json
def somedata():
    return dict(a=1, b=2)
