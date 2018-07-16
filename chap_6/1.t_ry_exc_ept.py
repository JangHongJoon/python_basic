'''
try:
    <예외가 발생할 가능성이 있는 코드>
except:
    <예외가 발생했을 때 코드>

'''


try :
    number=int(input())

    print("원의 반지름:", number)
    print("원의 반지름:", 2*3.14*number)
    print("원의 넓이:", 3.14*number*number)

except:
    print("Something's wrong")