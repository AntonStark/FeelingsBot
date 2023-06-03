import random
from datetime import datetime


def random_date_today() -> datetime:
    random_hour = int(random.triangular(15, 19)) - 3     # -3 because of timezones
    random_minute = random.randint(0, 59)
    datetime_ = datetime.today().replace(hour=random_hour, minute=random_minute)
    return datetime_
