X,Y={},{}
for _ in range(int(input())):
 x,y=map(int,input().split())
 if x in X:X[x].append(y)
 else:X[x]=[y]
 if y not in Y:Y[y]=0
 else:Y[y]+=1
print(sum(sum(Y[j]for j in X[i])*(len(X[i])-1)for i in X))
