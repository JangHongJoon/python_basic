#리스트를 선언합니다
array=[273,32,103,"문자열",True,False]
#리스트를 출력합니다
print(array)

#리스트의 요소를 출력합니다
print(array[4])

#리스트의 요소를 변경합니다
array[0]="changed"
print(array)

#리스트를 연산합니다
b=[1,2,3]
output=array+b
print(output)

#리스트의 요소를 제거합니다
del output[0:3]
print(output)