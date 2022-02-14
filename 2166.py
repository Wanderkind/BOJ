a=[];b=[];A=B=0;n=int(input())
for _ in range(n):x,y=map(int,input().split());a+=[x];b+=[y]
for i in range(n):A+=a[i-1]*b[i];B+=a[i]*b[i-1]
print(abs((A-B)/2))
