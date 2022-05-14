import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
n,k=U()
print(n*(n-1)/2/k)
