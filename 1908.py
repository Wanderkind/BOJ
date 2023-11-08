n = int(input())
d = 0
k = 1
while True:
    if 10**k <= n:
        d += k*9*10**(k - 1)
        k += 1
    else:
        d += k*(n - 10**(k - 1) + 1)
        break
r = pow(2, n - 1, 10000)
print(((n + 2)*r + 3*n - 4 + d*(r + 1)) % 10000)
