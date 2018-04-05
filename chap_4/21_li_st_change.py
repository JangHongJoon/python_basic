#변수를 선언
a="문자열"
b={"key":"moek", "key2":"maksd"}
c=range(10)

print("list({})={}.".format(a,list(a)))
#문자열 글자하나하나가 리스트 요소로
print("list({})={}.".format(b,list(b)))
#딕셔너리 키가 요소로 변환
print("list({})={}.".format(c,list(c)))
#범위에 속하는 정수가 요소로 변환

print()

example_list=["a","b","c"]
print(enumerate(example_list))
print(list(enumerate(example_list)))
