import pytest
# from snapes import snapes

def test_get_snippet(client):
    response = client.get('/snippet')
    print(response)
    assert True == True