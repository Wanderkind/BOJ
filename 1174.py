L=[[1,1,1,1,1,1,1,1,1,1]]
for i in range(1,11):
 L+=[[]]
 for j in range(10-i):
  z=0
  for k in range(j+1):z+=L[i-1][k]
  L[i]+=[z]
x=int(input())-1
if x>1022:print(-1);exit()
i=-1;w=1
while w>0:
 i+=1;j=-1
 while 1:
  j+=1
  if j>=10-i:break
  s=L[i][j]
  if x>=s:x-=s
  else:w=0;break
d=i+j
while i>0:
 i-=1;j=-1
 while 1:
  j+=1
  if j>=10-i:break
  s=L[i][j]
  if x>=s:x-=s
  else:w=0;break
 d=d*10+i+j
print(d)
