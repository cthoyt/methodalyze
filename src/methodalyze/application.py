# -*- coding: utf-8 -*-

"""

How to run in development mode

:code:`python3 -m methodalyze.application`

"""

from flasgger import Swagger
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_security import Security, SQLAlchemyUserDatastore

from methodalyze.models import User, Role, db, Statement, Method, Evaluation
from methodalyze.views import ui, api

swagger = Swagger()
security = Security()
bootstrap = Bootstrap()


def create_application():
    """Creates the Methodalyze Flask app

    :rtype: flask.Flask
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'methodalyze_secret_key'

    db.init_app(app)
    db.create_all(app=app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    security.init_app(app, user_datastore)
    swagger.init_app(app)
    bootstrap.init_app(app)

    admin = Admin(app)  # can make this only accessible to admin later
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Statement, db.session))
    admin.add_view(ModelView(Method, db.session))
    admin.add_view(ModelView(Evaluation, db.session))

    app.register_blueprint(ui)
    app.register_blueprint(api)

    return app


if __name__ == '__main__':
    app = create_application()
    app.run(debug=True)
