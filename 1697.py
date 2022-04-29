a,b=map(int,input().split())
if a>b:
    print(a-b)
else:
    s=[a]
    L=[[a]]
    t=0
    while 1:
        t+=1
        l=[]
        for i in L[-1]:
            for j in [i-1,i+1,2*i]:
                if 0<j<b+t and j not in s and j not in l:
                    l.append(j)
                    s.append(j)
        L.append(l)
        if b in l:
            print(t)
            break
