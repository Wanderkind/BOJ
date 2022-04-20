def f(i,j):
 m=max(abs(i),abs(j))
 if i==m:k=m-j
 elif i==-m:k=5*m+j
 else:z=j>0;k=(3+4*z)*m+(2*z-1)*i
 return str((2*m+1)**2-k)
R,C,r,c=map(int,input().split())
for i in range(R,r+1):print(' '.join([' '*(max(map(len,[f(R,C),f(R,c),f(r,C),f(r,c)]))-len(f(i,j)))+f(i,j)for j in range(C,c+1)]))
