from flask_login import login_required

from .. import {{cookiecutter.module_name}}_api_bp


@{{cookiecutter.module_name}}_api_bp.route("/somedata")
@login_required
def somedata():
    return dict(a=1, b=2)
