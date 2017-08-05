"""Evaluate the reproducibility of scientific protocols."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# metadata
__version__ = '0.1.0-dev'

__title__ = 'methodalyze'
# keep the __description__ synchronized with the module docstring
__description__ = 'Evaluate the reproducibility of scientific protocols.'
__url__ = 'https://github.com/scolby33/methodalyze'

__author__ = 'Scott Colby'
__email__ = 'scolby33@gmail.com'

__license__ = 'All rights reserved.'
__copyright__ = 'Copyright (c) 2017 Scott Colby'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from . import views
from . import models

# __all__ = []
