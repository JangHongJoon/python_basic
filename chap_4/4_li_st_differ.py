#리스트 선언
list_a=[1,2,3]

#연결 연산자
output=list_a + list_a #리스트 원본(list_a) 에 영향을
                        #주지 않음
print("# 리스트 연결 연산자 사용")
print("원본 리스트 : ",list_a)
print("연산 결과 : ",output)
print()



#extend() 함수로 리스트 연결
output = list_a.extend([1,2,3]) #리스트 원본에 영향을 줌

print("#extend() 함수 사용")
print("원본 리스트:" ,list_a)
print("연산 결과:" ,output)