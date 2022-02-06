import math
i=int(input());k=1+math.ceil(-1/2+(2*i+1/4)**(1/2));l=1-i+k*(k-1)//2
[a,b]=[l,k-l]if k%2==0 else[k-l,l]
print(f'{a}/{b}')
