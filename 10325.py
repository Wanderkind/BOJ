import sys
input=sys.stdin.readline

for _ in range(int(input())):
    M=0
    e=0
    for i in range(int(input())):
        a,b,c=map(int,input().split())
        x=b/a/2
        y=c+x*(b-a*x)
        if y>M:
            M=y
            e=i+1
    print(e)
