from flask import jsonify
from flask_security import login_required, current_user

from . import app
from . import db
from .models import Method, Evaluation


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/evaluate/<int:method_id>/<int:likert>', method=('POST'))
@login_required
def evaulate(method_id, likert):
    """Evaluates a method on the Likert scale

    Uses SQLAlchemy to look up the method by identifier then makes an instance of the Evaluation model in order
    to store the information linking the user, method, and the Likert.
    ---
    parameters:
      - name: method_id
        in: path
        description: The database identifier of the method to evaluate
        required: true
        type: integer
      - name: likert
        in: path
        description: The Likert value to assign to the method
        required: true
        type: integer
    responses:
      200:
        description: The summary of the action
    """
    method = Method.query.get(method_id)

    evaluation = Evaluation(
        value=likert,
        method=method,
        user=current_user,
    )

    db.session.add(evaluation)
    db.session.commit()

    return jsonify({
        'method': {
            'id': method.id
        },
        'evaluation': {
            'id': evaluation.id,
            'value': evaluation.value
        },
        'user': {
            'id': current_user.id,
            'email': current_user.email
        }
    })
