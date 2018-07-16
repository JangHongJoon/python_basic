memo=[0 for i in range(41)]
memo[0],memo[1]=(1,1)

def f(x):
    if x<=1 :
        return memo[x]
    else:
        if memo[x]>0 :
            return memo[x]

    memo[x]=f(x-1)+f(x-2)

T=int(input())
for i in range(T):
    N=int(input())
    if N==0 : print(1,0)
    elif N==1 : print(0,1)
    else :
        f(N)
        print(memo[N-2],memo[N-1])