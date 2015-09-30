import datetime
date = datetime.date(1901, 1, 1)
days = 0
while date.year < 2001:
    if date.weekday() == 6 and date.day == 1:
        days += 1
    date += datetime.timedelta(days=1)
print 'Sundays that fell on the first month during the twentieth century was {}'.format(days)