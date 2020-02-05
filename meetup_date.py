import datetime
import calendar
from Enum import enum

week_start = {
    1: 1,
    2: 8,
    3: 15,
    4: 22
}

class Weekday(enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

def meetup_date(year, month, nth=4, weekday=3):
    month_days = calendar.monthcalendar(year,month)
    if nth < 1:
        month_days = reversed(month_days)
        nth = abs(nth)
    count = 0
    for week, week_range in enumerate(month_days):
        if week_range[weekday] != 0:
            count += 1
            if count == nth:
                day = week_range[weekday]
    return datetime.date(year, month, day)

    # for day in range(week_start[nth],week_start[nth]+7):
    #     if datetime.date(year,month,day).weekday() == weekday:
    #         return datetime.date(year, month, day)