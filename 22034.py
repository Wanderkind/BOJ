tones=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
sharp=[1,3,6,8,10]

def f(i):
    if '#' not in i:
        t=tones.index(i[0])
        o=int(i[1:]) 
    else:
        t=tones.index(i[:2])
        o=int(i[2:])
    return 12*o+t

n=int(input())
w=[f(i) for i in input().split()]
l=[f(i) for i in input().split()]

lo=w[0]-min(l)
hi=w[1]-max(l)

if (lo>hi):
    exit(print('0 0'))

A,B=divmod(lo,12)
a,b=divmod(hi,12)

cnt=[sum(z%12 in sharp for z in [j+i for j in l])for i in range(12)]
if A==a:
    C=cnt[B:b+1]
    m=min(C)
    print(m,C.count(m))
elif A+1==a:
    C=cnt[B:]+cnt[:b+1]
    m=min(C)
    print(m,C.count(m))
else:
    C=cnt[B:]+cnt[:b+1]
    m=min(C+cnt)
    print(m,cnt.count(m)*(a-A-1)+C.count(m))
