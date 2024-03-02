from datetime import timedelta
from auth.config import Config
from auth.util import now

def user_expires_at():
    return now() + timedelta(days=Config.USER_DEFAULT_EXPIRY_TIME)
