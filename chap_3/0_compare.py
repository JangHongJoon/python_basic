print(10 == 100) #같은가
print(10 != 100) #다른가
print(10 < 100) #오른쪽 피연산자가 큰가
print(10 > 100) #오른쪽 피연산자가 작은가
print(10 <= 100) #오른쪽 피연산자가 크거나 같은가
print(10 >= 100) #오늘쪽 피연산자가 작거나 같은가
print()
print()

'''
결과값

False
True
True
False
True
False

'''
import sys
a="1"
print(sys.getsizeof(a),type(a), end='') #파이썬 이어쓰기 - >end=''
print(sys.getsizeof("B"))

print(sys.getsizeof("하마"))
print("가방" =="가방")
print("가방" !="하마")
print("가방" < "하마")
print("가방" > "하마")

'''
바이트 크기 출력 함수

import sys
sys.getsizeof()
'''

