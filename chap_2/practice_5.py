radius=float(input("반지름 : "))
surround="{:g}".format(radius*2*3.14)
area="{:g}".format(radius*radius*3.14)
print("둘레 :" ,surround)
print("넓이 :" ,area)

print()

print(type(surround)) #포맷하면 str 자료형이 된다
print(type(area)) #안 하면 float 자료형이 된다
