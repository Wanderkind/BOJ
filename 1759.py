from itertools import combinations as q
v,c=[],[]
L,C=map(int,input().split())
l=sorted(input().split())
for i in l:
    if i in ['a','e','i','o','u']:
        v.append(i)
    else:
        c.append(i)
for i in q(l,L):
    if len(set(i)&set(v))>0 and len(set(i)&set(c))>1:
        print(''.join(i))
