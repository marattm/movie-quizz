# services/quizz/project/__init__.py
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the application
app = Flask(__name__)

# instantiate db
db = SQLAlchemy(app)


def create_app(script_info=None):
    # instatiate app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprint
    from project.api.quizz import quizz_blueprint
    app.register_blueprint(quizz_blueprint)

    # shell context, flask.cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
