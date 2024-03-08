# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    lis=list(map(int,input().split()))
    motu=[]
    tomu=[]
    for j in range(n):
        if j%2==0:motu.append(lis[j])
        else:tomu.append(lis[j])
    motu.sort()
    motu=motu[::-1]
    tomu.sort()
    st=0
    sm=0

    for j in motu:sm+=j
    for j in tomu:st+=j
    j=0
    if st>sm:
            print('YES')
    else:
        while j<k and j<len(tomu):
            st+=motu[j]
            st-=tomu[j]
            sm+=tomu[j]
            sm-=motu[j]
            j+=1

        if sm>=st:
            print('NO')
        else:
            print('YES')
