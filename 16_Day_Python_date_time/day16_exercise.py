# Exercises: Day 16
# Get the current day, month, year, hour, minute and timestamp from datetime module
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# Today is 5 December, 2019. Change this time string to time.
# Calculate the time difference between now and new year.
# Calculate the time difference between 1 January 1970 and now.

from datetime import datetime, date, timedelta
now = datetime.now()
timestamp = now.timestamp()
print(now)
print(timestamp)

mod_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(mod_date)

date_str = "5 December, 2019"
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)

today = date(2022, 7, 29)
new_year = date(2023, 1, 1)
diff = new_year - today
print(diff)

t1 = date(1970, 1, 1)
new_diff = today - t1
print(new_diff)