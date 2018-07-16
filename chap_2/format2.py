output_f="{:+d}".format(52) #양수
output_g="{:+d}".format(-52) #음수
output_h="{: d}".format(52) #양수 : 기호 부분 공백
output_i="{: d}".format(-52) #음수 : 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

'''
{:+d} + 기호 추가는 양수와 음수 기호 따라 붙힘
'''

#조합하기
output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
