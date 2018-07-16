'''
elif 구문 ->
두가지만으로 구분되지 않는 조건에서 사용
'''
import datetime
now = datetime.datetime.now()
month=now.month

if 3<=month<=5:
    print("현재는 봄입니다")

if 6<=month<=8:
    print("현재는 봄입니다")

if 9<=month<=11:
    print("현재는 가을입니다")

if 12<=month<=2:
    print("현재는 겨울입니다")

'''
*프로그래밍은 조건문으로 도배한다!@
'''