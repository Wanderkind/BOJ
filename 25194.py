from collections import Counter
input()
l=[i%7 for i in[*map(int,input().split())]]
c=Counter(l)
e=[[(i*j)%7 for j in range(min(c[i]+1,7))]for i in c]
L=[]
C=len(e)
for i in e[0]:
    if C<2:
        L.append(i%7)
    if C>1:
        for j in e[1]:
            if C<3:
                L.append((i+j)%7)
            if C>2:
                for k in e[2]:
                    if C<4:
                        L.append((i+j+k)%7)
                    if C>3:
                        for l in e[3]:
                            if C<5:
                                L.append((i+j+k+l)%7)
                            if C>4:
                                for m in e[4]:
                                    if C<6:
                                        L.append((i+j+k+l+m)%7)
                                    if C>5:
                                        for n in e[5]:
                                            if C<7:
                                                L.append((i+j+k+l+m+n)%7)
                                            if C>6:
                                                for o in e[6]:
                                                    L.append((i+j+k+l+m+n+o)%7)
print(['NO','YES'][4 in L])
