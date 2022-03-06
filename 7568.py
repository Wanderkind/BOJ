a,b,n=[],'',int(input())
for i in range(n):a+=[[*map(int,input().split())]]
for i in a:
 z=1;x,y=i
 for j in a:p,q=j;z+=int(x<p and y<q)
 b+=str(z)+' '
print(b)
