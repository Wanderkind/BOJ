R=range
n=int(input())//5
I=input()
L=[''.join([I[e*n+i]for e in R(5)])for i in R(n)]
l=[[]]
for i in L:
 if'.'*5==i:l+=[[]]
 else:l[-1]+=[i]
def h(z):return''.join(['#.'[i%2]*int(z[i])for i in R(len(z))])
def f(z):return''.join(z)if z!=[]else''
def g(z):return str([*map(h,['636','5','114111411','111121116','34125','312111213','6111213','14145','61116','3121116'])].index(z))if z!=''else''
print(''.join([*map(g,map(f,l))]))
