# services/quizz/project/__init__.py
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the application
app = Flask(__name__)

# instantiate db
db = SQLAlchemy(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


# model
class User(db.Model):
    __tablename__ = "high_score"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    img = db.Column(db.String(128), nullable=False)
    label_name = db.Column(db.String(128), nullable=False)
    label_nb = db.Column(db.Integer, nullable=False)

    def __init__(self, name, img, label_name, label_nb):
        self.username = username
        self.email = email
        self.label_name = label_name
        self.label_nb = label_nb

# route
@app.route('/quizz/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
