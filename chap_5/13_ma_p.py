# 함수를 선언합니다.

def power(item):
    return item * item
def under_3(item):
    return item<3

#변수를 선언합니다.
list_input_a=[1,2,3,4,5]

#map() 함수를 사용 합니다.
output_a = map(power,list_input_a)
print(list(output_a))
output_a=filter(under_3,list_input_a)
print(list(output_a))