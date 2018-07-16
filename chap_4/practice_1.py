list_a=[52,273,103,32,57]
min=max=list_a[0]
for i in range(1,len(list_a)):
    if min>list_a[i]: min=list_a[i]
    if max<list_a[i]: max=list_a[i]
print("최소값:",min)
print("최대값:",max)
