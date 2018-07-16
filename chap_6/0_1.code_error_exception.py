number=input()

if number.isdigit():
    number = int(input())

    print("원의 반지름:", number)
    print("원의 반지름:", 2*3.14*number)
    print("원의 넓이:", 3.14*number*number)

else :
    print("정수 입력 please")
