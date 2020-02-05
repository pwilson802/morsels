import datetime
import calendar

class Weekday(object):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def meetup_date(year, month, nth=4, weekday=3):
    month_days = calendar.monthcalendar(year,month)
    if nth < 1:
        month_days = reversed(month_days)
        nth = abs(nth)
    count = 0
    for week_range in month_days:
        if week_range[weekday] != 0:
            count += 1
            if count == nth:
                day = week_range[weekday]
    return datetime.date(year, month, day)

    # for day in range(week_start[nth],week_start[nth]+7):
    #     if datetime.date(year,month,day).weekday() == weekday:
    #         return datetime.date(year, month, day)