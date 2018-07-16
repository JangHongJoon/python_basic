#메모화 - > 기하급수적으로 많이 반복한다는 문제 가 있다 -> 그래서 문제 해셜 방법
'''
처음에는 토끼가 한 쌍만 존재한다
두 달 이상된 토끼는 번식할 수 있다.
번식한 토끼는 매달 새끼를 한 쌍씩 낳는다.
토끼는 죽지 않는다고 가정한다.
'''
counter=0

def f(month):
    print("f({})를 구합니다.".format(month))
    global counter # global - > 함수 외부에 있는 변수를 참조 하기 위해 씀
    counter+=1
    if month ==1:
        return 1
    if month ==2:
        return 1
    else :
        return f(month-1)+f(month-2)

print("f(10):" ,f(10))
print("---")
print("f(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))

'''
트리 구조로 이루어진 재귀 함수에
노드 값을 덧셈을 한번씩 일일이 다 해주어야 하기 때문에
계산 횟수가 기하급수적으로 늘어난다.
'''