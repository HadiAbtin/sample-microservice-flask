from datetime import datetime
from pytz import timezone, utc
from auth.config import Config

def now(name=Config.TIMEZONE):
    tz = timezone(name)
    return datetime.now(tz=tz)
