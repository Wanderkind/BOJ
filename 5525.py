a,b,S,l,y=int(input()),int(input()),input(),[],-3
for i in range(b-2):
 if S[i]+S[i+1]+S[i+2]=='IOI':
  if y==i-2:l[-1]+=1
  else:l.append(2)
  y=i
print(sum([(i-a)*(i>a)for i in l]))
