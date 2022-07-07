from math import log2
n,p=map(int,input().split())
f=lambda x:'{:.6f}'.format(round(x,6))
if n==1:print('0.000000')
elif n==2:print(f(-log2(p/180)))
else:print(f(n-1-log2(n)+(1-n)*log2(p/180)))
