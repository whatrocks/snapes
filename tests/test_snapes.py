import pytest

import snapes

@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """
    app = create_app({
        'TESTING': True
    })
    yield app


@pytest.fixture
def client(app):
    yield app.test_client()