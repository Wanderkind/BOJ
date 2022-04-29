import sys
input=sys.stdin.readline
l=[]
N=int(input())
L=[[i]for i in range(N)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    L[a-1].append(b-1)
    L[b-1].append(a-1)
for i in range(N):
    L[i]=set(L[i])
for i in range(N-1,-1,-1):
    z=L[:]
    del z[i]
    if L[i] in z:
        del L[i]
y=L[:]
while 1:
    for i in range(len(L)):
        for j in range(len(L)):
            if len(L[i]&L[j])>0:
                L[i]=L[j]=L[i]|L[j]
    if L==y:
        break
    else:
        y=L[:]
for i in range(len(L)-1,-1,-1):
    z=L[:]
    del z[i]
    if L[i] in z:
        del L[i]
for i in L:
    if 0 in i:
        print(len(i)-1)
