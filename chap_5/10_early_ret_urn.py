dictionary={
    1:1,
    2:1
}
def f(n):
    if n  in dictionary :
        return dictionary[n]

    output = f(n-1)+f(n-2)
    dictionary[n]=output
    return output

'''
흐름 중간에 return 키워드를 사용하면 조기 리턴
(else 구문 없이)
'''