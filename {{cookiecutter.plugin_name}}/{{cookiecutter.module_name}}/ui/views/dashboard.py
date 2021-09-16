from flask_login import login_required

from flexmeasures.ui.utils.view_utils import render_flexmeasures_template

from ... import {{cookiecutter.module_name}}_ui_bp


@{{cookiecutter.module_name}}_ui_bp.route("/")
@{{cookiecutter.module_name}}_ui_bp.route("/dashboard")
@login_required
def dashboard():
    msg = "This is my plugin dashboard."

    return render_flexmeasures_template(
        "{{cookiecutter.module_name}}_dashboard.html",
        message=msg,
    )
