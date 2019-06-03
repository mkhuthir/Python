#!/usr/bin/python3

# A timedelta is used for a duration, or the time difference between two dates or times
# ---------------------------
# datetime.timedelta(days, seconds, microseconds)
# A timedelta can also be multiplied or divided by an integer or float

from datetime import datetime, timedelta, date, time

d1 = date(2011, 6, 15)
d2 = date(2012, 9, 18)
td = d2 - d1

print('Date 1 is',d1)
print('Date 2 is',d2)
print('time delta is ', td)
print('time delta in seconds ', td.total_seconds())
print('time delta type is ', type(td),end='\n\n')

today = datetime.today().date()

my_event = date(2021, 11, 6)

days_to_event = abs(my_event - today)

print(days_to_event.days, 'days to event.')
print(days_to_event, 'to event.')