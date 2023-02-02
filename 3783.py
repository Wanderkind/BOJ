from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

n=100 ###### input number of digits here ######

def flr(x):
    if '.' in x:
        x=str(x)
        return x[:x.index('.')]
    else:
        return x

def dc(a,n):
    a=str(a)
    n=int(n)
    if '.' in a:
        p=n-len(a)+a.index('.')+1
        if p>0:
            a+='0'*p
        if p<0:
            a=a[:p]
    else:
        a+='.'+'0'*n
    return a

def add(a,b):
    a=str(a)
    b=str(b)
    l=list(str(int(dc(a,n).replace('.',''))+int(dc(b,n).replace('.',''))).zfill(n+1))
    l.insert(-n,'.')
    if l[0]+l[1]=='-.':
        l[1]='0.'
    return ''.join(l)

def ndiv(A,q):
    a=list(str(A))
    b=flr(str(q))
    B=len(b)
    
    if '.' in a:
        p=len(a)-a.index('.')-1
        a.remove('.')
        c=len(a)
    else:
        p=0
        c=len(a)
    
    a+=['0']*(n+B-p)
    if c-p>=B:
        l=[]
        for i in range(len(a)-B):
            s=''
            u=int(i>0)
            for j in range(-u,B):
                s+=a[i+j]
            l+=[str(int(s)//int(b))]
            z=str(int(s)%int(b)).zfill(B+u)
            for j in range(-u,B):
                a[i+j]=z[j+u]
        l.insert(c-p-B+1,'.')
    else:
        l=['0','.']+['0']*(p+B-c-1)
        for i in range(len(a)-B):
            s=''
            u=int(i>0)
            for j in range(-u,B):
                s+=a[i+j]
            l+=[str(int(s)//int(b))]
            z=str(int(s)%int(b)).zfill(B+u)
            for j in range(-u,B):
                a[i+j]=z[j+u]
    
    while 1:
        if l[0]=='0' and l[1]!='.':
            del l[0]
        else:
            break
    
    return ''.join(l[:l.index('.')+1+n])

def mul(a,b):
    a=str(a)
    b=str(b)
    l=list(str(int(dc(a,n).replace('.',''))*int(dc(b,n).replace('.',''))).zfill(2*n+1))[:-n]
    l.insert(-n,'.')
    if l[0]+l[1]=='-.':
        l[1]='0.'
    return ''.join(l)

def exp(x,k):
    y = x
    for i in range(k-1):
        y=mul(y,x)
    return y

def compare(a, b): # is a greater than b?
    
    p = a.index('.')
    q = b.index('.')
    
    A = int(a[:p])
    B = int(b[:q])
    if A > B:
        return True
    if A < B:
        return False
    
    return int(dc(a, n)[p+1:]) > int(dc(b, n)[q+1:])

########################################

def sol():
    
    i = input()
    s = dc(i, n)
    
    l = dc(0, n); r = s
    for _ in range(1000):
        t = ndiv(add(l, r), 2)
        thr = exp(t, 3)
        if compare(thr, s):
            r = t
        else:
            l = t
    
    print("1.0000000000" if i == "1" else t[:-90])

for _ in range(int(input())):
    sol()
