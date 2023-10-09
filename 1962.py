import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *

exclude = {
    'ㄱ': ([6, 9], [2], [2, 4, 8, 9, 12]),
    'ㄴ': ([], [3], [1, 9]),
    'ㄹ': ([1, 7, 8], [], []),
    'ㅁ': ([3], [], [1]),
    'ㅂ': ([], [1, 2], []),
    'ㅅ': ([3, 4], [1], []),
    'ㅇ': ([1, 2, 5, 6], [], [2, 4, 7, 10]),
    'ㅈ': ([], [], [3, 6, 10, 11]),
    'ㅊ': ([7], [3], []),
    'ㅍ': ([8], [], []),
    'ㅎ': ([], [], [5]),
    'ㅏ': ([3, 4, 8], [], [1, 6, 9]),
    'ㅐ': ([], [2], [5, 11]),
    'ㅑ': ([], [], [7]),
    'ㅓ': ([], [3], [2, 10]),
    'ㅕ': ([], [], [4]),
    'ㅗ': ([5], [], [3]),
    'ㅜ': ([9], [], [8]),
    'ㅠ': ([6], [], []),
    'ㅡ': ([], [], [12]),
    'ㅣ': ([1, 2, 7], [1], [])
}

for _ in range(int(input())):
    
    n, m = U()
    jamo = input().split()
    
    e1 = [*range(10)]
    e2 = [*range(4)]
    e3 = [*range(13)]
    
    for x in jamo:
        p, q, r = exclude[x]
        for i in p:
            if i in e1: e1.remove(i)
        for i in q:
            if i in e2: e2.remove(i)
        for i in r:
            if i in e3: e3.remove(i)
    
    k1 = len(e1)
    k2 = k1**len(e2)
    
    if e1 == [0] or n >= k2**len(e3):
        print(-1)
        continue
    
    ans = 0
    y = 0
    while n:
        o = n % k2
        temp = 0
        z = 0
        while o:
            temp += e1[o % k1]*10**e2[z]
            o //= k1
            z += 1
        ans += temp*10000**e3[y]
        n //= k2
        y += 1
    
    print(ans)
