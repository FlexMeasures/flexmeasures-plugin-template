from flask import url_for


def test_view_responds(client):
    dashboard = client.get(
        url_for("{{cookiecutter.module_name}}_ui_bp.dashboard"), follow_redirects=True
    )
    assert dashboard.status_code == 200
 