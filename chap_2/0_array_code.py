print("안녕하세요") #큰 따옴표는 큰 따옴표로
print('안녕하세요') #작은 따옴표는 작은 따옴표로 끝냅니다.
print("안녕하세요"[0:4]) #범위 지정 출력도 가능해요
print(len("안녕하세요")) #길이 측정도 가능해요
print("")
a = "안녕하세요"
b=list(a)
print(b,type(b))
b = ''.join(a) 
print(b,type(b))    