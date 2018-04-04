#입력 받음
number=input("정수 입력 >")
number = int(number) # 정수로 변환

#양수 조건 
if number>0: #콜론 붙혀줍시다
    print("양수입니다")
    
#음수 조건 
if number<0:
    print("음수입니다")
#0 조건
if number==0:
    print("0입니다")

'''
if 를 쓰면 들여쓰기가 자동으로 TAB 키 없이도 됨

TAB키를 누르면 자동으로 띄어쓰기 4개를 넣어줌
->소프트 탭(soft tab)

들여쓰기 제거 -> Shift + TAB
여러 줄 들여쓰기 제거 -> 여러 줄 선택 후 Shift + TAB

https://goo.gl/xXjQqa
'''