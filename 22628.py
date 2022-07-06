import itertools as I
S=[
[4,5,0,1,6,7,2,3],
[2,3,6,7,0,1,4,5],
[1,5,3,7,0,4,2,6],
[4,0,6,2,5,1,7,3],
[1,3,0,2,5,7,4,6],
[2,0,3,1,6,4,7,5]
]
def f(l,p): return [l[S[p-1][i]] for i in range(8)]
def g(l,x,y): return f(f(l,x),y)
def h(l):
    C=[
    l,g(l,3,1),g(l,4,5),g(f(l,5),5,1),g(g(f(l,5),5,1),3,1),g(g(f(l,5),5,1),4,5),
    f(l,4),g(f(l,4),3,6),g(f(l,4),4,1),g(l,1,1),g(g(l,1,1),3,6),g(g(l,1,1),4,1),
    f(l,1),g(f(l,1),3,2),g(f(l,1),4,6),g(l,4,4),g(g(l,4,4),3,2),g(g(l,4,4),4,6),
    g(l,5,5),g(g(l,5,5),3,5),g(g(l,5,5),4,2),f(l,2),g(f(l,2),3,5),g(f(l,2),4,2)]
    return sorted([tuple(i) for i in C])[0]
print(len(set([h(i) for i in I.permutations(input().split())])))
