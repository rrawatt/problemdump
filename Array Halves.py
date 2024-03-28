t=int(input())
for i in range(t):
    n=int(input())
    perm=list(map(int,input().split()))
    a,b=n,n+1
    pos=0
    swap=0

    for j in range(-1,-(n+1),-1):
        if perm[j]<=n:
            pos=(2*n+j)
            break

    if pos!=0:
        for j in range(2*n-1,n,-1):
            if perm[j]>n and j<pos:
                swap+=pos-j
                pos-=1

    for j in range(n-1,-1,-1):
        if perm[j]>n:
            swap+=pos-j
            pos-=1
    print(swap)
  
