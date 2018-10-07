from datetime import datetime
from flask_login import current_user
from ..models import Twitt


def item_to_twitt(row):
    return Twitt(
        id=row['id'],
        text=row['text'],
        created_at=datetime.strptime(
            row['created_at'],
            '%a %b %d %H:%M:%S %z %Y'
        ),
        user_id=current_user.id
    )
