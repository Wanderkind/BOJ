import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import
#from random import *
#from functools import *


n = int(input())
board = [[*U()] for _ in range(n)]
diagboard = [[0]*(2*n - 1) for _ in range(2*n - 1)]
for i in range(n):
    for j in range(i + 1):
        if board[i - j][j]:
            diagboard[i][n - i + 2*j - 1] = 1
for i in range(n - 1):
    for j in range(n - i - 1):
        if board[n - 1 - j][i + j + 1]:
            diagboard[n + i][i + 2*j + 1] = 1

vc = [[] for _ in range(2*n - 1)]
cnt = 0
for i in range(2*n - 1):
    for j in range(2*n - 1):
        if diagboard[i][j]:
            vc[i].append(j)
            cnt += 1

if not cnt:
    print(0); exit()

vc1 = [[x//2 for x in l] for l in vc[::2]]
vc2 = [[x//2 for x in l] for l in vc[1::2]]

ans = 0

selected = [-1]*n
for i in range(n):
    vs = [False]*n
    def bimatch(N):
        if vs[N]:
            return False
        vs[N] = True 
        for num in vc1[N]:
            if selected[num] == -1 or bimatch(selected[num]):
                selected[num] = N
                return True
        return False
    bimatch(i)
    
for i in range(n):
    ans += selected[i] >= 0

selected = [-1]*(n - 1)
for i in range(n - 1):
    vs = [False]*(n - 1)
    def bimatch(N):
        if vs[N]:
            return False
        vs[N] = True 
        for num in vc2[N]:
            if selected[num] == -1 or bimatch(selected[num]):
                selected[num] = N
                return True
        return False
    bimatch(i)

for i in range(n - 1):
    ans += selected[i] >= 0

print(ans)
