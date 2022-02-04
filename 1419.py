import math
l=int(input());r=int(input());k=int(input())
if k%2==0:k//=2
x=r//k-math.ceil(l/k)+1
if k==1:
 for i in range(2):
  if l<=[1,2][i]<=r:x-=1 
elif k==3:
 if l<=3<=r:x-=1
elif k==2:
 for i in range(5):
  if l<=[2,4,6,8,12][i]<=r:x-=1
else:
 for i in range(2):
  if l<=[5,10][i]<=r:x-=1
print(x)
