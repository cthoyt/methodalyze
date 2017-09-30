# -*- coding: utf-8 -*-

import logging

from flask import jsonify, Blueprint, request, redirect, render_template, flash, request
from flask_security import login_required, current_user
from methodalyze.forms import MethodEvaluationForm
from methodalyze.models import db, Method, Evaluation

log = logging.getLogger(__name__)

ui = Blueprint('ui', __name__)
api = Blueprint('api', __name__)


@ui.route('/', methods=['GET', 'POST'])
def evaluate():
    form = MethodEvaluationForm()

    if not form.validate_on_submit():
        log.warning('gotta build the form: %s, %s', request.form, request.args)
        flash('hanging')
        return render_template('evaluate.html', form=form, current_user=current_user)

    log.warning('process results')

    flash('Form: {}'.format(form))
    render_template('evaluate.html')
    # return redirect(url_for('api.evaluate', method_id=0, likert=0, next=url_for('evaluate')))


@api.route('/evaluate/<int:method_id>/<int:likert>')
@login_required
def evaluate(method_id, likert):
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

    if 'next' in request.args:
        return redirect(request.args['next'])

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
