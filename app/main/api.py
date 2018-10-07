from flask_login import current_user
from ..auth.oauth import OAuthSignIn


def get_current_user_satuses():
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {
        'screen_name': current_user.username,
        'count': 10,
    }
    twitter = OAuthSignIn.get_provider('twitter')
    oauth_session = twitter.service.get_session(
        current_user.get_access_token()
    )
    response = oauth_session.get(url, params=params).json()
    return response
