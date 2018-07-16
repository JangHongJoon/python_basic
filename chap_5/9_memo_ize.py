#메모화
'''
재귀 함수의 연산속도가 느리다는 단점을 보완하기 위해
dictionary를 사용하여 연산이 되어있는 값은 값을
찾아간다. ( 중복 제거)
'''
dictionary = {
    1:1,
    2:2
}

def f(n):
    if n in dictionary :
        return dictionary[n]
    else :
        output = f(n-1)+f(n-2)
        dictionary[n]=output
        return output

print(f(10))
print(f(20))
print(f(30))
print(f(40))
print(f(50))
