while 1:
 try:p,q,r,s,t=input();A=p+q;B=s+t;x,y=sorted([abs(ord(p)-ord(s)),abs(int(q)-int(t))]);z=4 if(len({'a1','a8','h1','h8'}.intersection({A,B}))>0)*(x==y==1)else int('032214323223234343434434345454545456'[y*(y+1)//2+x]);print(f'To get from {A} to {B} takes {z} knight moves.')
 except EOFError:break
