from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check to make sure / works in the URL
    resp = app.request("/")
    assert_response(resp)

    # test our first GET request to /game to run the GameEngine
    resp = app.request("/game")
    assert_response(resp)
