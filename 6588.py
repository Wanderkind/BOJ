import math
def P(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:return False
    return True
l=list(filter(P,range(3,1000000)))
while 1:
    z=int(input())
    if z==0:break
    else:
        a,b,y=0,len(l),-1
        while 1:
            t=(a+b)//2
            if l[t]<z:a=t
            else:b=t
            if t!=y:y=t
            else:break
        while 1:
            w=0
            while l[w]+l[y]<z:w+=1
            if l[w]+l[y]==z:break
            else:y-=1
        print(f'{z} = {l[w]} + {l[y]}')
