def f(n):
 x=0
 for i in range(12,0,-1):k=(5**i-1)//4;x+=(n//k)*(5**i);n%=k
 return x
n=int(input());print(f(n)if f(n)!=f(n+1)else-1)
