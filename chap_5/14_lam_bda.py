# 함수를 선언합니다.

power=lambda x:x*x
under_3= lambda x: x<3


#변수를 선언합니다.
list_input_a=[1,2,3,4,5]

#map() 함수를 사용 합니다.
output_a = map(power,list_input_a)
print(list(output_a))
output_a=filter(under_3,list_input_a)
print(list(output_a))