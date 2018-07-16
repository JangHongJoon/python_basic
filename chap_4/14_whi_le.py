i=0
while i<10:
    print("{}번째 반복입니다".format(i))
    i+=1

#변수를 선언합니다.
list_test={1,2,1,2}
value=2

#list_test 내부에 value 가 있다면 반복
while value in list_test:
    list_test.remove(value)
