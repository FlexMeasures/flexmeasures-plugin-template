from flask import url_for


def test_get_somedata_needs_authtoken(client):
    response = client.get(
        url_for("{{cookiecutter.plugin_name}} API.somedata"),
        headers={"content-type": "application/json"},
        follow_redirects=True
    )
    assert response.status_code == 401  # HTTP error code 401 Unauthorized.
    assert "application/json" in response.content_type
    assert "not be properly authenticated" in response.json["message"]

    
# TODO: The somedata endpoint requires authentication to be testes successfully.
#       We'll need to add a user in conftest, which also requires us to add a db to testing
