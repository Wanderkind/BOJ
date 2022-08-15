n=int(input())
l=[]
for _ in range(n):
    l.append([*map(int,input().split())])
for i in range(n-1):
    for j in range(3):
        l[i+1][j]+=min(l[i][j-1],l[i][j-2])
print(min(l[-1]))
