#값으로 제거하기

list_c = [1,2,1,2] 
list_c.remove(2) #2가 두 개인데 왜 앞에 것만 없어질까
                #그것은 왼쪽에서 부터 발견되는 순서로 
                 #없애기 때문이다

print("remove(2):",list_c)

#모두 제거하기
list_d=[0,1,2,3,4,54]
list_d.clear() #모든 요소 제거
print(list_d)