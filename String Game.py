for i in range(int(input())):
    n=int(input())
    stra=input()
    x=min(stra.count('0'),stra.count('1'))
    if x%2==0:
        print('Ramos')
    else:
        print('Zlatan')
