a=[1]
temp=a[0]
cnt=0
i=0
while i<len(a):
    if temp==a[i]:
        cnt+=1
    
    elif temp!=a[i]:
        a.insert(temp,cnt)
        cnt=0
        temp=a[i]
    i+=1

if (cnt!=0): a.append(cnt)
print(a)