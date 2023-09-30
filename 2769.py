import sys
input = lambda: sys.stdin.readline().strip()
from itertools import product


isvar = lambda x: 96 < ord(x) < 123
binop = ['&', '^', '|']
sapling = lambda x: [None, False, x, None, None]

for h in range(int(input())):
    
    l = list(input())
    trees = []
    variables = sorted(set(filter(isvar, l)))
    ln = len(variables)
    
    prc = 3
    tree = sapling(3)
    neg = False
    negstack = []
    while l:
        c = l[0]
        target = tree
        
        if isvar(c):
            while isinstance(target[4], list):
                target = target[4]
            if target[0] == None:
                target[0] = c
                target[1] = neg
            else:
                trees.append(tree)
                tree = sapling(3)
                continue
            neg = False
        
        elif c == '(':
            while isinstance(target[4], list):
                target = target[4]
            if target[0] == None:
                prc += 4
                target[2] = prc
            else:
                trees.append(tree)
                tree = sapling(3)
                continue
        
        elif c == ')':
            if negstack:
                ns = negstack[-1]
                if ns == prc:
                    while target[2] <= ns - 4:
                        target = target[4]
                    target[1] = not target[1]
                    del negstack[-1]
            prc -= 4
        
        elif c == '~':
            neg = True
            while l[1] == '~':
                neg = not neg
                del l[0]
            if neg and l[1] == '(':
                negstack.append(prc + 4)
                neg = False
        
        elif c in binop:
            k = prc - binop.index(c) - 1
            def grow(t):
                if k <= t[2]:
                    return [c, False, k, t, sapling(prc)]
                else:
                    return t[:4] + [grow(t[4])]
            tree = grow(tree)
        
        del l[0]
    trees.append(tree)
    
    p0 = product("01", repeat = ln)
    p1 = set(product("01", repeat = ln - 1))
    
    def logic(tree):
        val, neg, prc, lft, rgt = tree
        
        if rgt == None:
            ind = variables.index(val)
            table = []
            for i in p1:
                case = list(i)
                case.insert(ind, "10"[neg])
                table.append(tuple(case))
            return set(table)
        
        else:
            a, b = logic(lft), logic(rgt)
            newset = eval('a' + val + 'b')
            if neg:
                return set(p0) - newset
            return newset
    
    print(f"Data set {h + 1}: {'Equivalent' if logic(trees[0]) == logic(trees[1]) else 'Different'}")
