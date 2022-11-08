def q(N):
    t,n,k=0,0,3
    while 1:
        n=2*n+k
        if N<=n:
            if N<=t+k:
                return N==t+1
            return q(N-t-k)
        k+=1;t=n
print('om'[q(int(input()))])
