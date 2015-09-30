#Abdulellah Hakim
import datetime
#set date to 1-JAN-1901
date = datetime.date(1901, 1, 1)
days = 0
while date.year < 2001:
	#if date is sunday and it is the first
    if date.weekday() == 6 and date.day == 1:
        days += 1
        #move to next date
    date += datetime.timedelta(days=1)
    #print
print 'Sundays that fell on the first month during the twentieth century was {}'.format(days)