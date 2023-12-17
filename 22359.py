import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
from itertools import product


t, k = U()

block = 2**(k - 1)

for _ in range(t):
    
    X, Y = U()
    X -= 1; Y -= 1
    x = [int(i) for i in bin(X)[2:].zfill(k)]
    y = [int(i) for i in bin(Y)[2:].zfill(k)]
    z = [2*x[i] + y[i] for i in range(k)]
    board = [['']*2**k for _ in range(2**k)]
    board[X][Y] = '@'
    
    sq = block
    u, v = sq - 1, sq - 1
    d = k - 1
    
    while d:
        if u <= X < u + 2 and v <= Y < v + 2:
            for g in range(u, u + 2):
                for h in range(v, v + 2):
                    if g != X or h != Y:
                        board[g][h] = 'a'
            break
        else:
            sq >>= 1
            d -= 1
            a = X > u; b = Y > v
            for g in range(2):
                for h in range(2):
                    if g != a or h != b:
                        board[u + g][v + h] = 'a' 
            u += (sq if a else -sq)
            v += (sq if b else -sq)
    
    z = z[:k - d - 1]
    
    def fill(ind, rf, cf, ev):
        l = len(ind)
        r, c = rf + block//2**(ev) - 1, cf + block//2**(ev) - 1
        for i in range(l):
            pp, qq = divmod(ind[i], 2)
            r += (1 if pp else -1)*2**(k - 2 - i - ev)
            c += (1 if qq else -1)*2**(k - 2 - i - ev)
        u = l - 1
        q = 0 < ind[u] < 3
        while u:
            if (0 < ind[u - 1] < 3) == q:
                u -= 1
            else:
                break
        rr, cc = divmod(ind[u], 2)
        for g in range(2):
            for h in range(2):
                if g != 1 - rr or h != 1 - cc:
                    board[r + g][c + h] = 'a'
    
    for rep in range(1, k - 1):
        for E in product((0, 1, 2, 3), repeat = rep):
            m = 0
            while m < rep:
                try:
                    if E[m] == z[m]:
                        m += 1
                    else:
                        break
                except IndexError:
                    break
            e = E[m:]
            rr, cc = 0, 0
            for q in range(m):
                gg, hh = divmod(E[q], 2)
                rr += gg*2**(k - q - 1)
                cc += hh*2**(k - q - 1)
            if e:
                fill(e, rr, cc, m)
    
    for i in range(2*block):
        o = (i//2) % 2
        for j in range(2*block):
            e = (j//2) % 2
            if not board[i][j]:
                board[i][j] = "cb"[o == e]
    
    for row in board:
        print(''.join(row))
