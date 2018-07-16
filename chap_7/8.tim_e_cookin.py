import datetime
now=datetime.datetime.now()
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y-%m-%d %H:%M:%S"))
