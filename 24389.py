n=int(input())
i=0
while (n%(2**(i+1)))//(2**i)<1:i+=1
print(31-i)
