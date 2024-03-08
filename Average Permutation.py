t=int(input())
for i in range(t):
    n=int(input())
    stra=''
    if n==3:
        print(1,2,3)
    elif n==4:
        print(4,1,2,3)
    else:
        for j in range(1,n-3):
            stra+=str(j)+' '
        print(str(n),str(n-3),stra+str(n-2),str(n-1))
