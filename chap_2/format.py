#숫자를 문자열로 바꿀 떄에는 format() 함수를 더 많이 사용함

#format() 함수로 숫자 ->문자열
format_output = "{}".format(52273)
print(type(52273),52273) #<class 'int'>
print(type(format_output),format_output) #<class 'str'>

print()
print()


#format() 함수 다양한 기본 형태

#숫자 -> 문자열
format_output_a="{}원".format(3000) #함수의 매개변수에 넣은 3000으로 대치
format_output_b="{} {} {}".format(1,2,3) #해당 위치에 맞게 대치
format_output_c="{} {} {}".format(1,"문자열",True) #숫자 이외에 다른 자료형도 적용 가능

print(format_output_a) 
print(format_output_b) 
print(format_output_c) 

print()
print()

'''
#'{}' 기호의 개수
"{} {}".format(1,2,3,4,5) #index out of Range
"{} {} {}".format(1,2) #error
'''

#정수
output_a="{:d}".format(52)

output_b="{:5d}".format(52) #5칸
output_c="{:10d}".format(52) #10칸
output_d="{:05d}".format(52)
output_e="{:05d}".format(-52)

print("#기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈 칸을 0으로 채우기")
print(output_d)
print(output_e)

