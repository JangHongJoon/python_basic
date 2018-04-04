array=[273,32,103,"문자열",True,False]
#print(array[6]) ->out of range

print(array)
'''
    리스트 출력 -> 내부 자료 모두 출력
    리스트 내부에 포함된 자료 -> 요소
'''

#리스트의 요소를 출력
print(array[0])
print(array[1])
print(array[2])
print(array[1:3]) # 범위 1번방에서 3번방까지

#리스트의 요소 변경
array[0]="변경" #0번방에 '273' 에서 '변경'
print(array)

#뒤에서부터 요소 선택
array=[273,32,103,"문자열",True,False]

print(array[-1])
print(array[-2])
print(array[-3])


