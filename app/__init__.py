from flask import Flask

from app.common.database import Database
from config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Register our blueprints
    from .default import default as default_blueprint
    app.register_blueprint(default_blueprint)

    # Initialize any extensions we are using
    bootstrap.init_app(app)
    Database.initialize()

    return app
