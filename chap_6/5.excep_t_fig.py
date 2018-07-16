list=[52,273,32,72,100]
'''
try:
    n=int(input("정수>"))
    print("{}번쨰 요소: {}".format(n,list[n]))
except Exception as exception:
    print("type(exception):",type(exception))
    print("exception:",exception)
'''

try:
    n=int(input("정수>"))
    print("{}번쨰 요소: {}".format(n,list[n]))
except ValueError as exception:
    print("exception:",exception)

except IndexError as exception:
    print("asdasdasdasd")
    print("exception:",exception)


'''
list=[52,273,32,72,100]

try:
    n=int(input("정수>"))
    print("{}번쨰 요소: {}".format(n,list[n]))
except ValueError:
    print("정수 입력")
except IndexError:
    print("범위 준수 입력")

'''