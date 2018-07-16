try :
    n=int(input("정수>"))
    print("원의 반지름:", n)
    print("원의 반지름:", 2*3.14*n)
    print("원의 넓이:", 3.14*n*n)

except Exception as exception:
    print("type(exception):",type(exception))
    print("exception:", exception)
