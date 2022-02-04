l=[]
for _ in range(4):l.append(list(map(int,input().split())))
def d(a,b):return((l[a][0]-l[b][0])**2+(l[a][1]-l[b][1])**2)**(1/2)
print(int(min([d(0,1)+d(1,2)+d(2,3),d(0,1)+d(1,3)+d(2,3),d(0,2)+d(1,2)+d(1,3),d(0,2)+d(2,3)+d(1,3),d(3,0)+d(2,3)+d(1,2),d(3,0)+d(1,3)+d(1,2)])))
