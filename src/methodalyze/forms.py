# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms.fields import RadioField, SubmitField

from methodalyze.models import Likert

equipment_text = 'This method defines the equipment used well enough to be accurately reproduced'
reagents_text = 'This method defines the reagents used well enough to be accurately reproduced'
procedure_text = 'This method defines the procedures used well enough to be accurately reproduced'
communication_text = 'This method communicates the results of the experiment'


def enum_radio(label):
    """Builds a RadioField

    :param str label: The label for the radio field
    :rtype: wtforms.fields.RadioField
    """
    return RadioField(
        label,
        choices=[
            (entry.value, entry.name.replace('_', ' ').title())
            for entry in Likert
        ]
    )


class MethodEvaluationForm(FlaskForm):
    """Builds a form for method evaluation on the likert scale"""
    equipment = enum_radio(equipment_text)
    reagents = enum_radio(reagents_text)
    procedure = enum_radio(procedure_text)
    communication = enum_radio(communication_text)

    submit = SubmitField('submit')
