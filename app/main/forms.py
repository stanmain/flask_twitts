# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The forms module from the main app."""

from flask_wtf import FlaskForm
from wtforms import SubmitField


class SubmitForm(FlaskForm):
    submit = SubmitField('Сохранить')
