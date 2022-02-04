for i in range(int(input())):
 a=0;b,c,d,e=map(int,input().split());n=int(input())
 for j in range(n):
  p,q,r=map(int,input().split())
  if((b-p)**2+(c-q)**2-r**2)*((d-p)**2+(e-q)**2-r**2)<0:a+=1
 print(a)
