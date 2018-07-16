#매개변수
'''
def <함수이름>(<매개변수>, <매개변수>, ...):
    <문장>
'''

def print_n_times(value, n):
    for i in range(n):
        print("{:2d}".format(i+1),value) #칸 맞추기 format 문 참조 -> "{:<숫자>d}"

print_n_times("안녕하세요" ,10)

