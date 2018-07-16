import datetime

now=datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")

output_c=now.strftime("%Y.%m.%d %H:%M:%S")
print(output_c)

