import random
from datetime import datetime


def random_datetime_today(hour_min: int, hour_max: int) -> datetime:
    datetime_ = datetime.today().replace(
        hour=int(random.triangular(hour_min, hour_max)) - 3,  # -3 because of timezones
        minute=random.randint(0, 59),
    )
    return datetime_
