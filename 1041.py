n=int(input());a,b,c,d,e,f=map(int,input().split())
if n<2:print(a+b+c+d+e+f-max(a,b,c,d,e,f))
else:print(min([a+b+c,a+b+d,a+c+e,a+d+e,f+b+c,f+b+d,f+c+e,f+d+e])*4+min([a+b,a+c,a+d,a+e,b+c,c+e,d+e,d+b,f+b,f+c,f+d,f+e])*(8*n-12)+min(a,b,c,d,e,f)*(n-2)*(5*n-6))
