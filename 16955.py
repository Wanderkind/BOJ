def f(z):
 r=0
 for i in range(5):s=['X']*5;s[i]='.';r+=int(''.join(s)in z)
 return int(r>0)
e,l=0,[]
for i in range(10):l+=[input()]
for i in range(10):
 s=''
 for j in range(10):s+=l[j][i]
 e+=f(s)+f(l[i])
for i in range(19):
 I,s,K,t=min(i,9),'',max(9-i,0),''
 for j in range(10-abs(i-9)):s+=l[I-j][i-I+j];t+=l[K+j][K+j+i-9]
 e+=f(s)+f(t)
print(int(e>0))
