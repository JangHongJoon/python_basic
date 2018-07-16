#가변 매개변수와 기본 매개변수 둘이 같이 가능?

#기본 매개면수가 가변 매개변수보다 앞에 올 때 - > 에러 뜸
'''
def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")


Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm 2017.3.4\helpers\pydev\pydevd.py", line 1668, in <module>
    main()
  File "C:\Program Files\JetBrains\PyCharm 2017.3.4\helpers\pydev\pydevd.py", line 1662, in main
    globals = debugger.run(setup['file'], None, None, is_module)
  File "C:\Program Files\JetBrains\PyCharm 2017.3.4\helpers\pydev\pydevd.py", line 1072, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "C:\Program Files\JetBrains\PyCharm 2017.3.4\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "C:/Users/PAUL/Desktop/Python/chap_5/4_keyword_param_eter.py", line 11, in <module>
    print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")
  File "C:/Users/PAUL/Desktop/Python/chap_5/4_keyword_param_eter.py", line 6, in print_n_times
    for i in range(n):
TypeError: 'str' object cannot be interpreted as an integer

'''

#가변 매개변수가 기본 매개변수보다 앞에 올 때 - > 가변 매개변수가 우선시 됨

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍",3)

#키워드 매개변수 - > 특정 매개변수의 이름을 지정해서 입력하는 매개변수 
def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("안녕하세요","즐거운","파이썬 프로그래밍", n=3)