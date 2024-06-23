n , k= map(int, input().split())
num=list(map(int, input().split()))
num.sort()

if k == 0:
    if num[0]==1:
       print("-1")
    else:
        print("1")
elif k==n:
    print(num[n-1])
else:
    if num[k-1]==num[k]:
        print("-1")
    else:
        print(num[k-1]) 


