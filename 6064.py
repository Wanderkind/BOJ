import math
for _ in range(int(input())):m,n,x,y=map(int,input().split());print(-1 if(x-y)%math.gcd(m,n,m-n)>0 else min(set([z*m+x for z in range(n)])&set([z*n+y for z in range(m)])))
