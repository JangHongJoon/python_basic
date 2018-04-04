'''

우리는 숫자가 짝수인지 홀수인지
맨 뒷자리 숫자를 보고
0,2,4,6,8 이면 짝수
아님 홀수
'''

#입력을 받죠
number=input("정수 입력 >")
number=int(number)

#문자열로 변환시켜 줍니다
number=str(number)

#마지막 자리 숫자를 호출
last_character=number[-1]
#숫자로 변환
last_number=int(last_character)

#짝수 확인
if last_number ==0\
    or last_number ==2\
    or last_number ==4\
    or last_number ==6\
    or last_number ==8:
    print("짝수입니다")

#홀수 확인
if last_number==1\
    or last_number ==3\
    or last_number ==5\
    or last_number ==7\
    or last_number ==9:
    print("홀수입니다")