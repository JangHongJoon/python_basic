def return_test():
    print("A 위치입니다.")
    return # 리턴합니다.
    print("B 위치입니다.")

return_test()

'''
return -> 함수를 실행했던 위치로 돌아가라

'''

#자료와 함께 리턴하기 - > return 옆에 자료를 붙혀주기

def return_test():
    return 100

value = return_test()
print(value)


#None - > return 옆에 아무것도 없으면 None 반환 

def return_test():
    return 

value = return_test()
print(value)

r