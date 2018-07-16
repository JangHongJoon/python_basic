#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now() #????

#출력
your_date=now.second
print(your_date)
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")

print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")


if now.hour < 12 : #콜론 꼭 붙혀줍시다.
    print("현재 시간은 {}시로 오전입니다!".format(now.hour))

if now.hour >= 12 :
    print("현재 시간은 {}시로 오후입니다!".format(now.hour))

    