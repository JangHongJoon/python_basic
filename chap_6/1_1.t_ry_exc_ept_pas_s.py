list=["52","273","32","tt","103"]

list_new=[]
for i in list:
    #숫자로 변환해서 리스트에 추가합니다.
    try:
        float(i)
        list_new.append(i)
    except:
        pass

print(list)
print(list_new)