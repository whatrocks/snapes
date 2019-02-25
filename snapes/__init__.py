from flask import Flask
from redis import Redis

from snapes.controllers.snippet import snippet
from snapes.fakeredis import FakeRedis

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # TODO: override for prod with config.py
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    if app.testing:
        app.redis = FakeRedis()
    else:
        app.redis = Redis(host="redis", port=6379, decode_responses=True)

    
    # register all api routes
    app.register_blueprint(snippet)
    
    return app