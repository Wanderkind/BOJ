n=int(input())
v=[[]for _ in range(n)]
for i in range(5):
    s=input()
    for j in range(n):
        for k in range(3):
            if s[4*j+k]=='.':
                v[j].append(3*i+k)
w=[[]for _ in range(n)]
for i in range(n):
    for j in range(10):
        if set([[4,7,10],[0,1,3,4,6,7,9,10,12,13],[3,4,10,11],[3,4,9,10],[1,4,9,10,12,13],[4,5,9,10],[4,5,10],[3,4,6,7,9,10,12,13],[4,10],[4,9,10]][j])-set(v[i])==set():
            w[i].append(j)
z=0
for i in range(n):
    W=w[i]
    if W==[]:
        exit(print(-1))
    z+=10**(n-1-i)*sum(W)/len(W)
print(z)
