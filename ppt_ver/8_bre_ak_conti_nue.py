numbers = [5,15,6,20,7,25,0,50]

#break 키워드는 반복문을 빠져나올 때 
#continue는 그 순간의 반복을 아무 실행 없이 넘길 때 
#사용합니다

for i in numbers :
    if i==0:
        break
    elif i%5 != 0:
        continue
    print(i)
