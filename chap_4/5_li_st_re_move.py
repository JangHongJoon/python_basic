list_a =[0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거하기")
print(list_a)
#제거 방법 1. => del
del list_a[1]
print("del list[1]:" ,list_a)

#제거 방법 2.=> pop()
list_a.pop(2)
print("pop(2):" ,list_a)
print()

'''
pop() 함수는 매개변수에 아무것도 넣지 않으면 pop(-1)
이 되어서 마지막 요소를 제거합니다.
'''

#범위 선택 요소 제거
list_b = [0,1,2,3,4,5,6]
del list_b[3:6] #마지막 6번째 방은 포함 X

print("# 인덱스로 리스트의 요소 여러 개를 제거하기")
print("del list_b[3:6]:", list_b)\


print("#인덱스로 리스트의 요쇼 한쪽 전부 제거하기")
list_b = [0,1,2,3,4,5,6] 
list_c = [0,1,2,3,4,5,6]
del list_b[:3] #:3 ->3-1번 방부터 요소 제거
del list_c[3:] #3: ->3+1번 방부터 요소 제거
print(list_b,"\n",list_c)
