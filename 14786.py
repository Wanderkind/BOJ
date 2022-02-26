import math
a,b,c=map(int,input().split())
x,n=((c/a)//math.pi+.5)*math.pi,1
for _ in range(99):
 n+=1
 x+=math.pi*(.5**n)if a*x+b*math.sin(x)<c else-math.pi*(.5**n)
print(x)
