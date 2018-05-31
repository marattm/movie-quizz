# services/project/api/quizz.py

from flask import Blueprint, jsonify

quizz_blueprint = Blueprint('quizz', __name__)


@quizz_blueprint.route('/quizz/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
