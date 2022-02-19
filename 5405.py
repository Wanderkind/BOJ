def f(x):
 x-=1;L=[]
 for i in range(n):L+=[x//(4**(n-1-i))];x%=4**(n-1-i)
 N=[[0,0]]
 for i in range(n):
  if L[n-1-i]<1:N+=[[-1/4+N[i][1]/2,-1/4+N[i][0]/2]]
  elif L[n-1-i]<2:N+=[[-1/4+N[i][0]/2,1/4+N[i][1]/2]]
  elif L[n-1-i]<3:N+=[[1/4+N[i][0]/2,1/4+N[i][1]/2]]
  else:N+=[[1/4-N[i][1]/2,-1/4-N[i][0]/2]]
 return N[n]
for _ in range(int(input())):n,h,o=map(int,input().split());d=((f(h)[0]-f(o)[0])**2+(f(h)[1]-f(o)[1])**2)**(1/2);print(round(d*10*2**n))
