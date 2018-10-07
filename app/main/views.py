# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the main app."""

from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from .. import db
from ..models import Twitt
from . import bp
from .api import get_current_user_satuses
from .forms import SubmitForm
from .utils import item_to_twitt


@bp.route('/')
@login_required
def index():
    response = get_current_user_satuses()
    query = db.session.query(Twitt.id)
    query = query.order_by(Twitt.created_at.desc())
    query = query.limit(10)
    twitt_in = query.all()
    twitt_in = tuple(item[0] for item in twitt_in)
    twitt_list = []
    for item in response:
        twitt = item_to_twitt(item)
        twitt_list.append(twitt)
    form = SubmitForm()
    return render_template(
        'index.html',
        title='Twitts',
        twitts=twitt_list,
        twitt_in=twitt_in,
        form=form,
    )


@bp.route('/save', methods=('POST',))
@login_required
def save():
    form = SubmitForm()
    if form.validate_on_submit():
        response = get_current_user_satuses()
        for item in response:
            twitt = item_to_twitt(item)
            db.session.merge(twitt)
        db.session.commit()
        flash('Твиты сохранены.')
    return redirect(url_for('main.index'))
