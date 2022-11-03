import sys
input=lambda:sys.stdin.readline().strip()

def sol():
    
    command=input()
    n=int(input())
    w=input()[1:-1]
    try:l=[*map(int,w.split(','))]
    except:l=[]
    
    q=[]
    r=0
    for i in command:
        if i=='R':
            r=-1-r
        else:
            q.append(r)
    
    for i in q:
        del l[i]
    if r:
        l.reverse()
    
    print(str(l).replace(' ',''))

for _ in range(int(input())):
    try:sol()
    except:print('error')
