n=int(input())
l=[*map(int,input().split())]
if len(l)>1 and len(set(l))==1:
    exit(print(l[0]))
elif n<3:
    exit(print('A'))
a,b,c=l[:3]
try:
    p=(c-b)//(b-a)
except ZeroDivisionError:
    exit(print('B'))
q=b-p*a
for i in range(2,n):
    if l[i-1]*p+q!=l[i]:
        exit(print('B'))
print(l[i]*p+q)
