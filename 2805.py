a,b=map(int,input().split())
s=[*map(int,input().split())]
l,r,y=0,max(s),-1
def f(x):
    return sum(max(0,i-x) for i in s)
while 1:
    t=l+(r-l)//2
    if t==y:
        exit(print(t))
    else:
        y=t
    if f(t)<b:
        r=t
    elif f(t)>b:
        l=t
    else:
        break
print(t)
