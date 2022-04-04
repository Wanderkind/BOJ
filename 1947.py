z=1
for n in range(1,int(input())+1):z=(n*z+(-1)**n)%10**9
print(z)
