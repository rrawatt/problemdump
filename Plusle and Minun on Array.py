t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(lambda x: abs(int(x)), input().split()))
    pos = [arr[i] for i in range(0, n, 2)]
    neg=[arr[i] for i in range(1,n,2)]
    mina=min(pos)
    maxa=max(neg)
    spos=sum(pos)
    sneg=sum(neg)

    res=spos-sneg+2*maxa-2*mina
    if res>spos-sneg:
        print(res)
    else:
        print(spos-sneg)


