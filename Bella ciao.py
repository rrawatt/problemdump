t=int(input())
for i in range(t):
    days,period,rate,rateinc=map(int,input().split())
    n=days//period
   
    monies=((rate*(n))+(n)*(n-1)//2*rateinc)*period

    rate+=((n)*rateinc)
    monies+=((days%period))*rate
    print(int(monies))
