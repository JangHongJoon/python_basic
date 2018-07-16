try:
    number=int(input("정수 입력>"))
    print("원의 반지름:", number)
    print("원의 반지름:", 2 * 3.14 * number)
    print("원의 넓이:", 3.14 * number * number)

except:
    print("정수 제발")
else:
    print("no 예외")

finally:
    print("일단은 끝났어")