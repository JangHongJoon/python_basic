#문자열 찾기
output_a="안녕안녕하세요".find("안녕")
output_b="안녕안녕하세요".rfind("안녕")

print("find():", output_a) #왼쪽에서 부터 -> 0:안 1:녕
print("rfind():",output_b) #오른쪽에서 부터 -> 2:안 3:녕
