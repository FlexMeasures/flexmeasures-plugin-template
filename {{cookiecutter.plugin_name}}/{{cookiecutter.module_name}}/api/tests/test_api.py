from flask import url_for


def test_get_somedata_needs_login(client):
    response = client.get(url_for("{{cookiecutter.plugin_name}} API.somedata"), follow_redirects=True)
    # TODO: this test requires auuthentication. Future work:
    # a) FM gives back HTML now, but after https://github.com/SeitaBV/flexmeasures/pull/210 it should be JSON
    # b) we should add a user, which also requires us to add a db to testing
    assert response.status_code == 200  # should be 401
    assert "text/html" in response.content_type  # response should be JSON
    assert b"Please log in" in response.data