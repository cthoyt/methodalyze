import enum

from . import db


class Likert(enum.Enum):
    strongly_disagree = 0
    disagree = 1
    neutral = 2
    agree = 3
    strongly_agree = 4


class Statement(db.Model):
    __tablename__ = 'statements'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)


class Method(db.Model):
    __tablename__ = 'methods'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    statements = db.relationship('Statement')


class Evaluation(db.Model):
    __tablename__ = 'evaluations'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Enum(Likert), nullable=False)
    method_id = db.Column(db.Integer, db.ForeignKey('methods.id'), nullable=False)
    statement_id = db.Column(db.Integer, db.ForeignKey('statements.id'), nullable=False)
