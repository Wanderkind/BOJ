import math
n=int(input())
for i in range(n):
 z='*'
 for j in range(round(math.log(n,3))):
  J=3**j
  if (i%(3*J))//J!=1:z*=3
  else:z=z+' '*J+z
 print(z)
