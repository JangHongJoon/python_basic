#for문으로 팩토리알 구하기
'''
def factorial(n):
    #변수를 선언합니다.
    output=1
    #반복문을 돌려 숫자를 더합니다.
    for i in range(1,n+1):
        output*=i
    #리턴합니다.
    return output


print("1!:",factorial(1))
print("2!:",factorial(2))
print("3!:",factorial(3))
print("4!:",factorial(4))
print("5!:",factorial(5))
'''

#재귀로 팩토리알 구하기

def fac(n):
    if n==1 :
        return 1
    return fac(n-1)*n

print("1!:" ,fac(1))
print("2!:" ,fac(2))
print("3!:" ,fac(3))
print("4!:" ,fac(4))
print("5!:" ,fac(5))
