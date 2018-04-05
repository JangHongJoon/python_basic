#변수를 선언합니다
'''
number=int(input("정수 입력>"))

if number%2==0:
    print("""\
    입력한 문자열은{}입니다.
    {}는 짝수입니다.""".format(number,number))

if number%2==0:
    print((
        "입력한 문자열은{}입니다.\n"
    "{}는 짝수입니다.")
    .format(number,number))

else:
    print((
        "입력한 문자열은{}입니다.\n"
    "{}는 홀수입니다.")
    .format(number,number))


test=(
    "이렇게 입력해도"
    "하나의 문자열로 연결되어"
    "생성됩니다."
)
print("test:",test)
print("type(test):",type(test))


test=(
    "이렇게 입력해도",
    "하나의 문자열로 연결되어",
    "생성됩니다.",
)
print("test:",test)
print("type(test):",type(test))

'''


print("::".join(["1","2","3","4","5"])) #문자열 사이사이

import textwrap

#여러 줄 문자열의 들여쓰기를 만들기 위해 구문을 사용해봅니다.
if True:
    #변수를 선언합니다.
    test="""\
    이런저런
    문자열을 
    생성해요"""

    print("-test:",test)
    print("-textwrap.dedent(test):",textwrap.dedent(test))