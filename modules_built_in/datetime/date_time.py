#!/usr/bin/python3

# Today's Date
# ---------------------------
# Use datetime.date.today()
# datetime.date class has the following integer attributes, date(year, month, day)
# get day of the week using date.weekday() # Monday is 0

from datetime import date
d1 = date.today()
print(d1)
print(d1.month, d1.day, d1.year)
print(d1.weekday())


# Comparison, addition and sutraction of dates
# ---------------------------
# Comparison gives boolean result. Later date is greater than earlier date.
# Date addition & subtraction give result as a datetime.timedelta object (explained more below).
# The same comparison and add/subtract operations can be used with time objects.

from datetime import date
d1 = date.today()
d2 = date(2015, 5, 14)
print(d1 > d2)
print(d1 - d2)

# Time
# ---------------------------
# time objects have the following attributes, time(hour, minute, second, microsecond, tzinfo)
# use datetime.time to compare time objects: t1 < t2 if t1 occurs before t2
# attributes are all optional, so you can just work with hours and minutes if you want
# daylight savings is handled by the time.dst() function (if tzinfo is set)

from datetime import time
t1 = time(14, 25, 36, 18625)
print(t1)

t2 = time(2, 19)
print(t2)
print(t1 < t2)

# datetime.datetime combines date and time attributes into a datetime object
# ---------------------------
# datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
# datetime.datetime objects can be used as dictionary keys
# includes functions: date(), time()

from datetime import datetime
dt1 = datetime(1941, 12, 7, 7, 53)
print(dt1)
print(dt1.date())
print(dt1.time())

# Use datetime.datetime.now() to get the current date and time

t3 = datetime.now()

print(t3.time())
print(t3.date())
print(t3.hour, t3.minute)
print(str(t3.month) + '-' + str(t3.day) + '-' + str(t3.year))

# Use datetime.strftime() to get names of months and weekdays.

t3 = datetime.now()
print(t3.strftime('%A'))
print(t3.strftime('%a, %A, %b, %B, %x'))



