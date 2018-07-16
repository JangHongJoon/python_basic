# 가변 매개변수 함수
'''
def <함수 이름< (<매개변수>, <매개변수>, ..., *<가변 매개변수>):
    <문장>

가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
가변 매개변수는 하나만 사용할 수 있다.
'''

def print_n_times(n,*values):
    #n번 반복합니다.
    for i in range(n):
        #values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

'''
print 함수 자동 완성 기능에

print (value, ..., sep= ' ', ...)

value는 가변 매개변수인데 왜 매개변수들이 올까?

-> 기본 매개변수라서 가능한 것
->기본 매개변수 뒤에는 일반 매개변수가 올 수 없다.
'''

#기본 매개변수

def print_n_times(value, n=2):
    for i in range(n):
        print(value)
print_n_times("안녕하세요")
'''
print_n_times 에서 n=2 라고 기본 값을 주었기 때문에 가능

만약 print_n_times(n=2,value) 형태로 사용하면, 
"안녕하세요" 를 어디다가 할당해야 하는지 확실하게 
알 수 없다. 
내부적을 그래서 기본 매개변수 뒤에 일반 매개변수는 불가능으로 막음
'''