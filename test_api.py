import pytest
import api as service

@pytest.fixture
def api():
    return service.api

def test_main(api):
    r = api.requests.get("/")
    assert r.text == "Wrong route, Mr. Potter! 10 points from Gryfinndor!"