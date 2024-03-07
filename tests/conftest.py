import pytest
from auth.auth import create_app

@pytest.fixture()
def app():
    app = create_app()
    return app



@pytest.fixture()
def client(app):
    app.testing = True
    return app.test_client()


