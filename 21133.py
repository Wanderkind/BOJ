n=int(input())
a,b=[*range(2,n+1,2)],[*range(1,n+1,2)]
if n%6==2:del b[2];b+=[5];del b[1];b=[3]+b
if n%6==3:del a[0];a+=[2];del b[1];del b[0];b+=[1,3]
for i in a+b:print(i)
