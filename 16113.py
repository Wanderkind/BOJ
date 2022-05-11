n=int(input())//5
I=input()
L=[''.join([I[e*n+i]for e in range(5)])for i in range(n)]
l=[[]]
for i in L:
 if i=='.....':l+=[[]]
 else:l[-1]+=[i]
def f(z):return''.join(z)if z!=[]else''
def g(z):return str(['######...######','#####','#.####.#.####.#','#.#.##.#.######','###....#..#####','###.##.#.##.###','######.#.##.###','#....#....#####','######.#.######','###.##.#.######'].index(z))if z!=''else''
print(''.join([*map(g,map(f,l))]))
