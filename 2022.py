x,y,c=map(float,input().split())
f=lambda d:(x*x-d*d)**-.5+(y*y-d*d)**-.5
l,r=0,min(x,y)
for _ in range(20):t=(l+r)/2;l,r=[[t,r],[l,t]][f(t)>1/c]
print(round(t,3))
