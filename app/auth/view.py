from flask import redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .oauth import OAuthSignIn
from .. import db
from ..models import User


@auth.route('/login')
def login():
    return render_template(
        'auth/login.html',
        title='Login'
    )


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли.')
    return redirect(url_for('auth.login'))


@auth.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@auth.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, token = oauth.callback()
    if social_id is None:
        flash('Ошибка аутентификации!')
        return redirect(url_for('main.index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(
            social_id=social_id,
            username=username,
            email=None,
            access_token_key=token[0],
            access_token_secret=token[1],
        )
        db.session.add(user)
    else:
        user.access_token_key = token[0]
        user.access_token_secret = token[1]
    db.session.commit()
    login_user(user, True)
    return redirect(url_for('main.index'))
