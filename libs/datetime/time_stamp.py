#!/usr/bin/python3

# Get a UNIX timestamp (time since the epoch)
# ---------------------------
# A timestamp is the time since Jan 1, 1970 in seconds
# Use time.time() to get timestamp
# Use datetime.fromtimestamp(ts) and datetime.timestamp(datetime_obj) to convert between timestamp and datetime

import time
ts = time.time()
print('current time stamp:',ts)
print('current time', time.ctime(ts))

from datetime import datetime
now = datetime.fromtimestamp(ts)
print(now)
print(datetime.timestamp(now))