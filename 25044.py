n,k=map(int,input().split())
z=1440*n
y=z+1440
L=[]
d=-1
while 1:
    d+=1
    l=[900+(1440+k)*(d-1),1080+(1440+k)*(d-1),1260+(1440+k)*(d-1)]
    if any(z<=i for i in l):
        L+=l
    if any(y<i for i in l):
        break
t=[i%1440 for i in L if z<=i<y]
print(len(t))
for i in t:
    a,b=map(str,divmod(i,60))
    print(f'{a.zfill(2)}:{b.zfill(2)}')
