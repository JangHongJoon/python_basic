b_year=int(input("태어난 년도 >"))
animal=b_year%12
if animal==0:
    print("원숭이",end='')
elif animal==1:
    print("닭",end='')
elif animal==2:
    print("개",end='')
elif animal==3:
    print("돼지",end='')
elif animal==4:
    print("쥐",end='')
elif animal==5:
    print("소",end='')
elif animal==6:
    print("범",end='')
elif animal==7:
    print("토끼",end='')
elif animal==8:
    print("용",end='')
elif animal==9:
    print("뱀",end='')
elif animal==10:
    print("말",end='')
elif animal==11:
    print("양",end='')
print("띠")
