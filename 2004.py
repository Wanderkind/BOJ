def f(x,k):
 y=0
 while x:x//=k;y+=x
 return y
a,b=map(int,input().split())
print(min(f(a,i)-f(a-b,i)-f(b,i)for i in[2,5]))
