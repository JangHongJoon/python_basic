#문자열 연산자의 우선순위
print("안녕" + "하세요" *3) #"하세요" *3 -> "안녕" +"하세요"

'''
꼭 먼저 연산되는 연산자는 괄호를 붙여줍시다!!
'''

#TypeError 예외
string ="문자열"
number=273
print(string+number) #서로 다른 자료는 연산 불가능 !!
