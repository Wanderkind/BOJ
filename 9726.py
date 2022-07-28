import sys
input=sys.stdin.readline

pos,neg=[],[]
zp=zn=0
for i in range(30):
    zp+=4**i
    pos.append(zp)
    zn+=2**(2*i+1)
    neg.append(zn)

for h in range(int(input())):
    n=int(input())
    if n==0:
        y=0
    elif n>0:
        for i in range(30):
            if n<=pos[i]:
                l=2*i
                break
        y='1'
        w=4**i
        for i in range(l-1,-1,-1):
            q=i//2-1
            if i%2:
                r=-neg[q] if 0<=q else 0
                if r<=n-w:
                    y+='0'
                else:
                    w+=(-2)**i
                    y+='1'
            else:
                r=pos[q] if 0<=q else 0
                if n-w<=r:
                    y+='0'
                else:
                    w+=(-2)**i
                    y+='1'
    else:
        n*=-1
        for i in range(30):
            if n<=neg[i]:
                l=2*i+1
                break
        y='1'
        w=-(-2)**(l)
        for i in range(l-1,-1,-1):
            q=i//2-1
            if i%2:
                r=neg[q] if 0<=q else 0
                if n-w<=r:
                    y+='0'
                else:
                    w-=(-2)**i
                    y+='1'
            else:
                r=-pos[q] if 0<=q else 0
                if r<=n-w:
                    y+='0'
                else:
                    w-=(-2)**i
                    y+='1'
    print(f'Case #{h+1}: {y}')
