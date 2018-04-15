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

    from app.models.users.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/users")

    from app.models.vehicles.views import vehicle_blueprint
    app.register_blueprint(vehicle_blueprint, url_prefix="/vehicles")

    from app.models.addresses.views import address_blueprint
    app.register_blueprint(address_blueprint, url_prefix="/addresses")

    # Initialize any extensions we are using
    bootstrap.init_app(app)
    Database.initialize()

    return app
