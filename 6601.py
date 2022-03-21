l=[
[0],
[3,2],
[2,1,4],
[3,2,3,2],
[2,3,2,3,4],
[3,4,3,4,3,4],
[4,3,4,3,4,5,4],
[5,4,5,4,5,4,5,6]]

while 1:
    try:
        p,q,r,s,t=input()
        A=p+q;B=s+t
        x,y=sorted([abs(ord(p)-ord(s)),abs(int(q)-int(t))])
        if len({'a1','a8','h1','h8'}.intersection({A,B}))>0 and x==y==1:
            z=4
        else:
            z=l[y][x]
        print(f'To get from {A} to {B} takes {z} knight moves.')
    except EOFError:
        break
