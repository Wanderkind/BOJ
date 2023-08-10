from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())


global n
n = int(input())

def push(four):
    for i in range(n - 1):
        if not sum(four[i:]):
            break
        z = n
        while not four[i]:
            z -= 1
            for j in range(i, n - 1):
                four[j] = four[j + 1]
            four[z] = 0
    return four

def alter(four):
    four = push(four)
    for i in range(n - 1):
        if not four[i] or four[i] != four[i + 1]:
            continue
        four[i] *= 2
        for j in range(i + 1, n - 1):
            four[j] = four[j + 1]
        four[n - 1] = 0
    return four

def down(mat):
    res = [0 for _ in range(n*n)]
    for x in range(n):
        a = alter([mat[x + y] for y in range(n*n-n, -n, -n)])
        for y in range(n):
            res[x + n*n-n - n*y] = a[y]
    return res

def up(mat):
    res = [0 for _ in range(n*n)]
    for x in range(n):
        a = alter([mat[x + y] for y in range(0, n*n, n)])
        for y in range(n):
            res[x + n*y] = a[y]
    return res

def left(mat):
    res = [0 for _ in range(n*n)]
    for x in range(0, n*n, n):
        a = alter(mat[x:x + n])
        for y in range(n):
            res[x + y] = a[y]
    return res

def right(mat):
    res = [0 for _ in range(n*n)]
    for x in range(0, n*n, n):
        a = alter(mat[x:x + n][::-1])
        for y in range(n):
            res[x + n - 1 - y] = a[y]
    return res

dulr = lambda mat: [down(mat), up(mat), left(mat), right(mat)]

m = []
for _ in range(n):
    m += [*U()]

ans = 0
for a in dulr(m):
    for b in dulr(a):
        for c in dulr(b):
            for d in dulr(c):
                for e in dulr(d):
                    x = max(e)
                    if x > ans:
                        ans = x

print(ans)
