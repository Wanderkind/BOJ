I=input;v=int
l=v(I());r=v(I());k=v(I())
k//=2-k%2
print(r//k-v((l+k-.1)/k)+1-sum(l<=[[1,2],[2,4,6,8,12],[3],0,[5,10]][k-1][i]<=r for i in range([2,5,1,0,2][k-1])))
