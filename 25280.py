import sys
input=sys.stdin.readline
l=[]
for _ in range(int(input())):
    l.append([*map(float,input().split())])
l.sort()
a,b=l[0]
c=((a+b)/2)
L=[]
i=0
while i<len(l)-1:
    i+=1
    if l[i][0]<c:
        L.append(l[i])
    else:
        break
if len(L)==0:
    exit(print((c)))
r=sorted([i[::-1]for i in L])[0][0]
def f(x):
    y=2
    for i in l:
        p,q=i
        if x<p:
            continue
        else:
            y*=(q-x)/(q-p)
    return y
for _ in range(50):
    t=(a+r)/2
    if f(t)>1:
        a=t
    else:
        r=t
print(t)
