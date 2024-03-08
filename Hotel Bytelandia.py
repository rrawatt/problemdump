def bina(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1

		else:
			return arr[mid]
	return -1

t=int(input())
for i in range(t):
    n=int(input())
    tim=[]
    arr=list(map(int,input().split()))
    dep=list(map(int,input().split()))
    arr.sort()
    dep.sort()
    tima=arr+dep
    fina=[]
    for k in tima:
        if k not in fina:
            fina.append(k)	
    fina.sort()		
    max=0
    coun=0
    for j in fina:
        if j==bina(arr,j):coun+=arr.count(j)
        if j==bina(dep,j):coun-=dep.count(j)
        if max<coun:max=coun
    if n==1:
        print(1)
    else:print(max)


