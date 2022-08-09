from itertools import permutations as p
l=[*map(int,input().split())]
w=l[0]
S=0
u=2**-.5
for i in p(l[1:],7):
    j=[w]+list(i)+[w,i[0]]
    s=0
    for k in range(1,9):
        p,t,q=j[k-1],j[k],j[k+1]
        s+=t*(p+q)*u>=p*q
    S+=s==8
print(S*8)
