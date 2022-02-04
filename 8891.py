import math
def c(i):k=math.ceil(-1/2+(2*i+1/4)**(1/2));l=-k*(k+1)//2;return[k+1,1-l-i]
for _ in range(int(input())):a,b=map(int,input().split());n=c(a)[0]+c(b)[0];print(n*(n-1)//2+1-c(a)[1]-c(b)[1])
