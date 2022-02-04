l=list(input());c=input()
for i in range(len(l)):
 if l[i]!=' ':l[i]=chr(97+(ord(l[i])-ord(c[i%len(c)])-1)%26)
print(''.join(l))
