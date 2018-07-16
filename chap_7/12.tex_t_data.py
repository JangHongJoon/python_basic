a=list("Python")
print("기본 문자열 :",a)

b=[]
for char in a:
    b.append(ord(char)) # 10진수 값 출력
print("10진수 :",b)

c=[]

for char in a:
    c.append(bin(ord(char)))
print("2진수 :",c)