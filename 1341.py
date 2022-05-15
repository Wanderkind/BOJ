a,b=map(int,input().split())
z=1
while(2**z-1)%b*(z<61):z+=1
print([-1,''.join(['-*'[int(i)]for i in bin(a*(2**z-1)//b)[2:].zfill(z)])][z<61])
