import math
n=int(input())
l=[*map(int,input().split())]
L=[]
y=0
for i in range(2*n-1):
    L.append(y)
    y+=(-1)**i*(l[i+1]-l[i])
L.append(y)
s=y+l[-1]
L.append(0)
l.append(s)
c=int(input())
for i in range(2*n+1):
    if c<=l[i]:break
d=l[i]-c
Y=L[i]+d*(-1)**i
try:z=max(math.ceil(Y+c*max([(L[j]-Y)/(c-l[j]) for j in range(i+(d!=0))])),0)
except:z=0
print(z)
