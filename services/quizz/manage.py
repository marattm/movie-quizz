# services/quizz/manage.py

from flask_cli import FlaskGroup

from project import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
