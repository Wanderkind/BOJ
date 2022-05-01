O=[
[i for i in range(36)],
[5-i//6+6*(i%6) for i in range(36)],
[35-i for i in range(36)],
[i//6+6*(5-i%6) for i in range(36)],
[5-i%6+6*(i//6) for i in range(36)],
[6*(i%6)+i//6 for i in range(36)],
[i%6+6*(5-i//6) for i in range(36)],
[35-(6*(i%6)+i//6) for i in range(36)]]
Z=[[6,7,8,9,12],[5,6,7,8,11],[4,5,6,7,10],[3,4,5,6,9],[5,6,7,8,12],[4,5,6,7,11],[1,2,4,5,6],[1,5,6,10,11],[1,4,5,6,10],[1,7,8,9,13],[5,6,7,13,14]]
for _ in range(3):
    l=[];v=0
    for i in range(6):l+=[*map(int,input().split())]
    while v<8:
        j=0;t=[]
        while 1:
            if l[O[v][j]]>0:b=j;break
            else:j+=1
        for j in range(1,36-b):
            if l[O[v][b+j]]>0:t+=[j]
        if t in Z:print('yes');break
        else:v+=1;continue
    if v>7:print('no')
