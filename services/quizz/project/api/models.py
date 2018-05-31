# services/quizz/project/api/models.py

from project import db

# model
class Quizz(db.Model):
    __tablename__ = "high_score"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    img = db.Column(db.String(128), nullable=False)
    label_name = db.Column(db.String(128), nullable=False)
    label_nb = db.Column(db.Integer, nullable=False)

    def __init__(self, name, img, label_name, label_nb):
        self.name = name
        self.img = img
        self.label_name = label_name
        self.label_nb = label_nb
