import random
from datetime import datetime


def random_datetime_today(hour_min: int, hour_max: int) -> datetime:
    # -3 because of timezones
    datetime_ = datetime.today().replace(
        hour=int(random.triangular(hour_min, hour_max)) - 3,
        minute=random.randint(0, 59),
    )
    return datetime_
