from flask import url_for


def test_view_responds(client):
    dashboard = client.get(
        url_for("{{cookiecutter.plugin_name}} UI.dashboard"), follow_redirects=True
    )
    assert dashboard.status_code == 200

