import pytest
import logging
import requests
from snapes import create_app
from ujson import loads
from unittest.mock import Mock, patch

logger = logging.getLogger(__name__)

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

def test_index(client):
    response = client.get("/")
    assert response.data == b'10 points from Gryfinndor!'
    assert response.status_code == 200

def test_get_snippet_fails_with_missing_url(client):
    response = client.get('/snippet',
        query_string={
            'max_age': 123
        }
    )
    assert response.status_code == 400

def test_get_snippet_fails_with_missing_max_age(client):
    response = client.get('/snippet',
        query_string={
            'url': 'https://www.holloway.com'
        })
    assert response.status_code == 400

def test_get_snippet_fails_with_missing_url_and_max_age(client):
    response = client.get('/snippet')
    assert response.status_code == 400

def test_get_snippet_from_cache(client):
    response = client.get('/snippet',
        query_string={
            'url': 'https://www.holloway.com',
            'max_age': 100
        })
    response_dict = loads(response.data)
    snippet = response_dict.get('snippet')
    assert response.status_code == 200
    assert snippet == 'I am the Holloway website!'

def test_get_snippet_not_in_cache(client):
    with patch('snapes.managers.scraper.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.text = '<p>Video games from the 1980s are the best</p>'
        response = client.get('/snippet',
            query_string={
                'url': 'https://www.atari.com',
                'max_age': 100
            })
        response_dict = loads(response.data)
        snippet = response_dict.get('snippet')
        assert response.status_code == 200
        assert snippet == 'Video games from the 1980s are the best...'