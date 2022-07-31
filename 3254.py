l=[[0,0,0,0,0,0]for _ in range(7)]
for q in range(21):
    a,b=map(int,input().split())
    z=-1
    while z<5:
        z+=1
        if l[a-1][z]==0:
            l[a-1][z]=1
            break
    for i in range(7):
        for j in range(3):
            if l[i][j:j+4]==[1,1,1,1]:
                exit(print('sk',q+1))
    for i in range(4):
        for j in range(6):
            if [l[i+k][j]for k in range(4)]==[1,1,1,1]:
                exit(print('sk',q+1))
    for i in range(4):
        for j in range(3):
            if [l[i+k][j+k]for k in range(4)]==[1,1,1,1]:
                exit(print('sk',q+1))
    for i in range(4):
        for j in range(3):
            if [l[i+3-k][j+k]for k in range(4)]==[1,1,1,1]:
                exit(print('sk',q+1))
    z=-1
    while z<5:
        z+=1
        if l[b-1][z]==0:
            l[b-1][z]=2
            break
    for i in range(7):
        for j in range(3):
            if l[i][j:j+4]==[2,2,2,2]:
                exit(print('ji',q+1))
    for i in range(4):
        for j in range(6):
            if [l[i+k][j]for k in range(4)]==[2,2,2,2]:
                exit(print('ji',q+1))
    for i in range(4):
        for j in range(3):
            if [l[i+k][j+k]for k in range(4)]==[2,2,2,2]:
                exit(print('ji',q+1))
    for i in range(4):
        for j in range(3):
            if [l[i+3-k][j+k]for k in range(4)]==[2,2,2,2]:
                exit(print('ji',q+1))
print('ss')
