#변수 선언
i=0

#무한 반복
while True:
    #몇 번째 반복인지 출력
    print("{}번째 반복문입니다".format(i))
    i=i+1
    #반복을 종료합니다
    input_text=input(">종료하시셌습니다까>(y): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다")
        break

#변수 선언
numbers=[5,15,6,20,7,25]

#반복을 돌립니다
for number in numbers:
    #number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number<10:
        continue
    print(number)

    '''
    continue 문은 들여쓰기를 한 개 줄여줘서
    효율적인 코딩이 가능하다.
    '''