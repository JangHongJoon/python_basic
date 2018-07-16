try:
    n=int(input("정수>"))
    print("{}번쨰 요소: {}".format(n,list[n]))
    예외.발생해주세요()
    
except ValueError as exception:
    print("exception:",exception)

except IndexError as exception:
    print("asdasdasdasd")
    print("exception:",exception)

except Exception as exception:
    print("미리 몰랐어요")
    print(type(exception),exception)