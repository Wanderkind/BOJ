O=[
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],
[5,11,17,23,29,35,4,10,16,22,28,34,3,9,15,21,27,33,2,8,14,20,26,32,1,7,13,19,25,31,0,6,12,18,24,30],
[35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
[30,24,18,12,6,0,31,25,19,13,7,1,32,26,20,14,8,2,33,27,21,15,9,3,34,28,22,16,10,4,35,29,23,17,11,5],
[5,4,3,2,1,0,11,10,9,8,7,6,17,16,15,14,13,12,23,22,21,20,19,18,29,28,27,26,25,24,35,34,33,32,31,30],
[0,6,12,18,24,30,1,7,13,19,25,31,2,8,14,20,26,32,3,9,15,21,27,33,4,10,16,22,28,34,5,11,17,23,29,35],
[30,31,32,33,34,35,24,25,26,27,28,29,18,19,20,21,22,23,12,13,14,15,16,17,6,7,8,9,10,11,0,1,2,3,4,5],
[35,29,23,17,11,5,34,28,22,16,10,4,33,27,21,15,9,3,32,26,20,14,8,2,31,25,19,13,7,1,30,24,18,12,6,0]]
Z=[[6,7,8,9,12],[5,6,7,8,11],[4,5,6,7,10],[3,4,5,6,9],[5,6,7,8,12],[4,5,6,7,11],[1,2,4,5,6],[1,5,6,10,11],[1,4,5,6,10],[1,7,8,9,13],[5,6,7,13,14]]
Y=[[5,3,4,1,2,0],[5,3,4,1,2,0],[5,3,4,1,2,0],[5,3,4,1,2,0],[5,3,4,1,2,0],[5,3,4,1,2,0],[2,4,0,5,1,3],[5,2,1,4,3,0],[5,3,4,1,2,0],[3,5,4,0,2,1],[4,3,5,1,0,2]]
l=[];v=0
for i in range(6):l+=[*map(int,input().split())]
while v<8:
    j=0;t=[]
    while 1:
        x=l[O[v][j]]
        if x>0:s=[x];b=j;break
        else:j+=1
    for j in range(1,36-b):
        x=l[O[v][b+j]]
        if x>0:s+=[x];t+=[j]
    if t in Z:print(s[Y[Z.index(t)][s.index(1)]]);exit()
    else:v+=1;continue
print(0)
