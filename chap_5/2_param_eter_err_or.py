#매개변수 넣지 않으면
def print_n_times(value,n):
    for i in range(n):
        print(value)
print_n_times("안녕하세요")
'''
Traceback (most recent call last):
  File "C:/Users/PAUL/Desktop/Python/chap_5/2_param_eter_err_or.py", line 5, in <module>
    print_n_times("안녕하세요")
TypeError: print_n_times() missing 1 required positional argument: 'n'
'''

#매개변수 더 많이 넣으면
def print_n_times(value,n):
    for i in range(n):
        print(value)
        
#함수를 호출합니다.
print_n_times("안녕하세요",10,20)

'''
Traceback (most recent call last):
  File "C:/Users/PAUL/Desktop/Python/chap_5/2_param_eter_err_or.py", line 15, in <module>
    print_n_times("안녕하세요",10,20)
TypeError: print_n_times() takes 2 positional arguments but 3 were given
'''