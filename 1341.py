a,b=map(int,input().split())
z=1
while(2**z-1)%b*(z<61):z+=1
s=bin(a*(2**z-1)//b)
print(''.join(['-*'[int(i)]for i in s[2:].zfill(z)])if z<61 else-1)
