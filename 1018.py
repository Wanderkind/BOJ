C=[];v='WBWBWBWB'
for _ in range(4):C+=[v,v[::-1]]
a,b=map(int,input().split());L=[]
for y in range(a):L.append(input())
l=[]
for j in range(a-7):
 for i in range(b-7):
  c=0
  for q in range(8):
   for p in range(8):
    if L[j+q][i+p]==C[q][p]:c+=1
  l.append(32-abs(c-32))
print(min(l))
