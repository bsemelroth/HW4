import pytest
from app import app as vtm_site

@pytest.fixture()
def app():
    yield vtm_site

@pytest.fixture
def client(app):
    return app.test_client()