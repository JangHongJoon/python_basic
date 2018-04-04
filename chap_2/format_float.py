#부동 소수점 출력의 다양한 형태
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273) # 15칸 만들기

output_c = "{:15f}".format(52.273) # 15칸 만들기
output_d = "{:+015f}".format(52.273) # 15칸 만들기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

print()
print()

#소수점 아래 자릿수 지정하기
output_a ="{:15.3f}".format(52.273) # 소수점 지정 방식 ->"{:15 .[원하는 자리수]f}".format(52.273)
print(output_a)

#의미없는 소수점 제거하기
print(0) #내부적으로 자료형이 다름
print(0.0)

output_a=52.0
output_b = "{:g}".format(52.0)
print(output_a)
print(output_b)
