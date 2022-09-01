import sys,math
input=sys.stdin.readline
n,r=map(int,input().split())
l=[int(input())%360000 for _ in range(n)]
s=math.comb(n,3)
j=-n+1
for i in range(n):
    v=l[i]
    while 1:
        w=(v-l[j])%360000
        if w<=180000:
            break
        j+=1
    s-=math.comb(i-j,2)
print(max(s,0))
