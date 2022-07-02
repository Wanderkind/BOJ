import math
for _ in range(int(input())):   
    a,b=map(int,input().split())
    k=b-a
    n=math.ceil((k+.25)**.5-.5)
    print(2*n-(k<=n*n))
