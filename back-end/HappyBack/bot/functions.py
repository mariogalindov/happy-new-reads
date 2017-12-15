import datetime 
from .models import Character

def set_snooze(minutes):
    now = datetime.datetime.now()
    snooze = now ++ datetime.timedelta(minutes=minutes)
    return (snooze)