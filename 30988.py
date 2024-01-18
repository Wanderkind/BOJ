import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter

n = int(input())
a = [*map(int, input().split())]

if n == 1: m = 1
elif n == 4: m = 2
elif n == 9: m = 3
elif n == 16: m = 4
elif n == 25: m = 5
else: exit(print(-1))

def pure():
    res = []
    for i in range(m + 1):
        r = [0]*(m + 1)
        r[i] = 1
        res.append([tuple(r)])
    return res

def mul(a, b):
    la = len(a)
    lb = len(b)
    res = [[] for _ in range(la + lb - 1)]
    for i in range(la):
        for k in a[i]:
            for j in range(lb):
                for l in b[j]:
                    res[i + j].append(tuple([k[u] + l[u] for u in range(m + 1)]))
    return res

def exp(a, t):
    def inner(b, u):
        if not u:
            return [[tuple([0]*(m + 1))]]
        return mul(inner(b, u - 1), b)
    return [Counter(r) for r in inner(a, t)]

def dictadd(a, b):
    res = {}
    for i in a:
        res[i] = a[i]
    for i in b:
        if i in res:
            res[i] += b[i]
        else:
            res[i] = b[i]
    return res

def add(a, b):
    la = len(a)
    for i in range(-1, -1 - la, -1):
        b[i] = dictadd(a[i], b[i])
    return b

square = [{}]
for i in range(m, -1, -1):
    e = exp(pure(), m - i)
    el = m*(m - i) + 1
    nw = [{} for _ in range(el)]
    for u in range(el):
        for k in e[u]:
            newk = list(k)
            newk[i] += 1
            nw[u][tuple(newk)] = e[u][k]
    square = add(square, nw)

def listprod(lst):
    res = 1
    for x in lst:
        res *= x
    return res

def apply(gc, d, lst):
    ln = len(lst)
    e = lambda k, x: d[k]*listprod(lst[i]**k[i] for i in range(ln))*x**k[ln]
    f = lambda x: sum(e(k, x) for k in d)
    return filter(lambda x: f(x) == gc, range(-100, 101))

def check(gc, d, lst):
    e = lambda k: d[k]*listprod(lst[i]**k[i] for i in range(m + 1))
    return sum(e(k) for k in d) == gc

def backtrack(acc, ind):
    if ind > n:
        print(m)
        exit(print(*acc))
    if ind <= m:
        for b in apply(a[ind], square[ind], acc):
            backtrack(acc + [b], ind + 1)
    else:
        if check(a[ind], square[ind], acc):
            backtrack(acc, ind + 1)

backtrack([], 0)
print(-1)
