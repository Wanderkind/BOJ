import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(100000)

mem = {}

def a(d, n):
    if not d or not n:
        return 1
    if (d, n) in mem:
        return mem[(d, n)]
    ans = a(d - 1, n) + a(d, n - 1)
    mem[(d, n)] = ans
    return ans

for _ in range(int(input())):
    N, M, n, m = map(int, input().split())
    print(sum(a(M, i)*a(N - M, n + 1 - i) for i in range(m + 1))/a(N + 1, n + 1))
