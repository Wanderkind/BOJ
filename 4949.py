while 1:
    i=input()
    if i=='.':
        exit()
    s=''
    for j in i:
        if j in ['(','[',')',']']:
            s+=j
    a,b=[0],[0]
    for j in s:
        if j=='(':
            a.append(a[-1]+1)
            b.append(b[-1])
        elif j=='[':
            a.append(a[-1])
            b.append(b[-1]+1)
        elif j==')':
            a.append(a[-1]-1)
            b.append(b[-1])
        else:
            a.append(a[-1])
            b.append(b[-1]-1)
    if any(i<0 for i in a)or any(i<0 for i in b):
        z=0
    else:
        if not a[-1]==b[-1]==0:
            z=0
        else:
            while 1:
                if '()'in s or '[]'in s:
                    s=s.replace('()','')
                    s=s.replace('[]','')
                    continue
                else:
                    break
            if'(]'in s or'[)'in s:
                z=0
            else:
                z=1
    print(['no','yes'][z])
