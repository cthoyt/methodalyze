# -*- coding: utf-8 -*-

import enum

from flask_security import RoleMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Likert(enum.Enum):
    """Enumerates the Likert Scale"""
    strongly_agree = 4
    agree = 3
    neutral = 2
    disagree = 1
    strongly_disagree = 0


class Method(db.Model):
    __tablename__ = 'methods'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)


class Statement(db.Model):
    __tablename__ = 'statements'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

    method_id = db.Column(db.Integer, db.ForeignKey('methods.id'), nullable=False)
    method = db.relationship('Method', backref=db.backref('statements'))


class Evaluation(db.Model):
    __tablename__ = 'evaluations'
    id = db.Column(db.Integer, primary_key=True)

    equipment = db.Column(db.Enum(Likert), nullable=False)
    reagents = db.Column(db.Enum(Likert), nullable=False)
    procedure = db.Column(db.Enum(Likert), nullable=False)
    communication = db.Column(db.Enum(Likert), nullable=False)

    method_id = db.Column(db.Integer, db.ForeignKey('methods.id'), nullable=False)
    method = db.relationship('Method')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('evaluations'))


roles_users = db.Table(
    'user_role',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


class User(db.Model, UserMixin):
    """Stores users"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    @property
    def admin(self):
        """Is this user an administrator?"""
        return self.has_role('admin')


class Role(db.Model, RoleMixin):
    """Stores user roles"""
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))
