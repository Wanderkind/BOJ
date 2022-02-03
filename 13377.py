import math
z='abcdefghi'
for _ in range(int(input())):
 l=input()
 m=1
 for i in range(8):
  n=0
  for j in range(i+1,9):
   if z.index(l[i])>z.index(l[j]):n+=1
  m+=n*math.factorial(8-i)
 print(m)
