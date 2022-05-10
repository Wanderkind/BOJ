X,Y={},{}
for _ in range(int(input())):
 x,y=map(int,input().split())
 if x in X:X[x]+=[y]
 else:X[x]=[y]
 if y in Y:Y[y]+=1
 else:Y[y]=0
print(sum(sum(Y[j]for j in X[i])*(len(X[i])-1)for i in X))
