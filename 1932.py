n=int(input())
l=[]
for _ in range(n):
    l.append([*map(int,input().split())])
for i in range(n-2,-1,-1):
    for j in range(i+1):
        l[i][j]+=max(l[i+1][j],l[i+1][j+1])
print(l[0][0])
