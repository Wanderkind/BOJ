from math import hypot as h

A, B, C = map(int,input().split())
a, b, c = map(int,input().split())

K = C/(A*A + B*B)
k = c/(a*a + b*b)

P, Q = K*A, K*B
p, q = k*a, k*b

H = lambda a, b, c, d: h(a, b) + h(c, d) + h(a - c, b - d)

if a*B == A*b:
    print(H(P, Q, p, q))
    exit()

x = (B*c - b*C)/(B*a - b*A)
y = (a*C - A*c)/(B*a - b*A)

def d(I, i):
    
    S = (I*x + (1 - I)*P)
    T = (I*y + (1 - I)*Q)
    s = (i*x + (1 - i)*p)
    t = (i*y + (1 - i)*q)
    
    return H(S, T, s, t)

u = [[0,0],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
I = i = 0.5
for z in range(20):
    w = 2**(-2 - z)
    while 1:
        l = [d(I + v[0]*w, i + v[1]*w) for v in u]
        m = min(l)
        if m != l[0]:
            X, Y = u[l.index(m)]
            I += X*w
            i += Y*w
        else:
            break

print(d(I, i))
