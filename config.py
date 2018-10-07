# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The config module from the Flask-Twitts app."""

import os


class Config:
    """Class of configuration parameters."""

    DEBUG = os.environ.get('DEBUG', False)
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT', False)
    JSON_AS_ASCII = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO', False)
    OAUTH = {
        'twitter': {
            'id': os.environ.get('CONSUMER_TOKEN_KEY'),
            'secret': os.environ.get('CONSUMER_TOKEN_SECRET')
        },
    }
