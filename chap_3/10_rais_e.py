number=input("")
number=int(number)

if number>0:
    raise NotImplementedError #Error를 일부러 띄워주는 !
else:
    raise  NotImplementedError #아직 구현을 하지 않은 것을
                                #얘기해 주는 에러문