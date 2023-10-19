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
diagboard = [[0]*(2*n) for _ in range(2*n - 1)]
for i in range(n):
    for j in range(i + 1):
        if board[i - j][j]:
            diagboard[i][n - i + 2*j] = 1
for i in range(n - 1):
    for j in range(n - i - 1):
        if board[n - 1 - j][i + j + 1]:
            diagboard[n + i][i + 2*j + 2] = 1

vc = [[0] for _ in range(2*n - 1)]
cnt = 0
for i in range(2*n - 1):
    for j in range(1, 2*n):
        if diagboard[i][j]:
            vc[i].append(j)
            cnt += 1

if not cnt:
    print(0); exit()

vc1 = vc[::2]
vc2 = vc[1::2]

stack = []
indexes = [0]*n
rw = 0
cnt = 0
ans1 = 0
while True:
    if rw == n:
        if cnt > ans1:
            ans1 = cnt
        rw -= 1
        try:
            del stack[-1]
        except IndexError:
            break
        cnt -= 1
        while not indexes[rw]:
            rw -= 1
        continue
    
    indexes[rw] += 1
    try:
        x = vc1[rw][indexes[rw]]
        if x not in stack:
            stack.append(x)
            rw += 1
            cnt += 1
    except IndexError:
        indexes[rw] = 0
        rw += 1

stack = []
indexes = [0]*(n - 1)
rw = 0
cnt = 0
ans2 = 0
while True:
    if rw == n - 1:
        if cnt > ans2:
            ans2 = cnt
        rw -= 1
        try:
            del stack[-1]
        except IndexError:
            break
        cnt -= 1
        while not indexes[rw]:
            rw -= 1
        continue
    
    indexes[rw] += 1
    try:
        x = vc2[rw][indexes[rw]]
        if x not in stack:
            stack.append(x)
            rw += 1
            cnt += 1
    except IndexError:
        indexes[rw] = 0
        rw += 1

print(ans1 + ans2)
