#range
for i in range(10):
    print(str(i)+"번째 반복입니다.")
print()
#리스트와 for문 조합
array=[273,32,103,57,52]
#리스트의 길이로 for문 범위 적용
for i in range(len(array)):
    print("{}번째 반복 : {}".format(1,array[i]))