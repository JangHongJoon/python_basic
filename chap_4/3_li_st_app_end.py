list_a=[1,2,3]
'''
append(), insert(), extend() 함수는 모두 
리스트에 직접적인 영향을 준다
'''


#append()
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4) #리스트 뒤에 '4'추가
print(list_a)
print()

#insert()
print("#리스트 중간에 요소 추가하기")
list_a.insert(0,10) #(0,10) ->0번쨰 위치에 10을 추가
print(list_a)

#extend() 
list_a=[1,2,3]
list_a.extend([4,5,6])#리스트 뒤에 확장을 해주는 역할
print("[1,2,3].extend([4,5,6]):",list_a)