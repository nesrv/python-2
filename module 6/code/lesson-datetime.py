from datetime import datetime, time, timedelta

birthday = datetime(2010, 1, 20)
date_now = datetime.now()

print(birthday)
print(date_now)
delta = date_now - birthday
print(delta.total_seconds()//60//60/24//30.3/12)

current_time = time(13,20)
hour = current_time.hour

hours_12 = timedelta(hours=12)

print(date_now + hours_12)
