# services/quizz/project/__init__.py

from flask import Flask, jsonify

# instantiate the application
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/quizz/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
