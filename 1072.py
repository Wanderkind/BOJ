x,y=map(int,input().split())
a=(100*y/x)%1
b=int(100*y/x)+1
if(99+a)*x!=100*y:k=int(((1-a)*(x**2))/((99+a)*x-100*y))
else:print(-1);exit()
if 99*x>100*y:
 if b*(x+k)==100*(y+k):print(k)
 else:print(k+1)
else:print(-1)
