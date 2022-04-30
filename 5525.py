a=int(input())
B=int(input())
b=B//2+2
S=input()
l=[]
y=-3
for i in range(B-2):
    if S[i]+S[i+1]+S[i+2]=='IOI':
        if y==i-2:
            l[-1]+=1
        else:
            l.append(1)
        y=i
print(sum([(i-a+1)*(i>=a)for i in l]))
