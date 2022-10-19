

############### globals ###############

p = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
M = [[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,2,3,1],[0,3,1,2],[0,3,2,1],[1,0,2,3],[1,0,3,2],[1,2,0,3],[1,2,3,0],[1,3,0,2],[1,3,2,0],[2,0,1,3],[2,0,3,1],[2,1,0,3],[2,1,3,0],[2,3,0,1],[2,3,1,0],[3,0,1,2],[3,0,2,1],[3,1,0,2],[3,1,2,0],[3,2,0,1],[3,2,1,0]]
Mr = [[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,3,1,2],[0,2,3,1],[0,3,2,1],[1,0,2,3],[1,0,3,2],[2,0,1,3],[3,0,1,2],[2,0,3,1],[3,0,2,1],[1,2,0,3],[1,3,0,2],[2,1,0,3],[3,1,0,2],[2,3,0,1],[3,2,0,1],[1,2,3,0],[1,3,2,0],[2,1,3,0],[3,1,2,0],[2,3,1,0],[3,2,1,0]]

############### function ###############

def decrypt(key,ciphertext): 
    
    V = len(key) 

    d0 = 0
    for u in range(V):
        b0 = ord(key[u])
        d0 = d0 + b0

    d1 = 0
    for u in range(V):
        b1 = ord(key[u])
        d1 = d1 + (2*u + 1)*b1

    d2 = 0
    for u in range(V):
        b2 = ord(key[u])
        d2 = d2 + ((-1)**u)*(b2 + u + 2)*b2

    d3 = 0
    for u in range(V):
        b3 = ord(key[u])
        d3 = d3 + (u + 3)*int(b3/(((13*b3)%11)%5 + 2))

    d4 = 0
    for u in range(V):
        b4 = ord(key[u])
        d4 = d4 + (u**3 + 6*u + (b4%23) + 4)*b4

    dd0 = (857*d0)%11383
    dd1 = (179*d1)%6257
    dd2 = (113*d2)%7873
    dd3 = (163*d3)%9811
    dd4 = (419*d4)%16369

    kl00 = []
    for t in range(6):
        tv = t + V
        j = ord((key[t]))
        k = ord(key[tv - 6])
        l = ord(key[int(V/2) + t - 3])
        kk = int((k - (k%100))/100)
        f = (tv**5 + tv**4 + 1012*(tv**3) + 18658*(tv**2) + 3429*tv + 199*j*k + 1319*j + 393*(k**2) + 5224*k + kk**2 + 174*kk + 673*l + 3*(dd0**2) + 146**dd0 + 286*(t**2) + 8431*t + d1*t)%10000
        sk = str(f).zfill(4)

        kl00.append(sk)

    kl01 = []
    for t in range(6):
        tv = t + V
        j = ord((key[t]))
        k = ord(key[tv - 6])
        l = ord(key[int(V/2) + t - 3])
        kk = int((k - (k%100))/100)
        f = (3*(tv**5) + 8*(tv**4) + 872*(tv**3) + 11846*(tv**2) + 2855*tv + 495*j*k + 233*j + 8239*(k**2) + 5108*k + 667*(kk**2) + 370*kk + 293*l + 5*(dd1**2) + 342**dd1 + 38*(t**2) + 509*t + d2*t)%10000
        sk = str(f).zfill(4)

        kl01.append(sk)

    kl02 = []
    for t in range(6):
        tv = t + V
        j = ord((key[t]))
        k = ord(key[tv - 6])
        l = ord(key[int(V/2) + t - 3])
        kk = int((k - (k%100))/100)
        f = (tv**5 + 4*(tv**4) + 1838*(tv**3) + 15868*(tv**2) + 3411*tv + 17*j*k + 431*j + 771*(k**2) + 8738*k + 11*(kk**2) + 88*kk + 1619*l + 11*(dd2**2) + 194**dd2 + 191*(t**2) + 902*t + d3*t)%10000
        sk = str(f).zfill(4)

        kl02.append(sk)

    kl03 = []
    for t in range(6):
        tv = t + V
        j = ord((key[t]))
        k = ord(key[tv - 6])
        l = ord(key[int(V/2) + t - 3])
        kk = int((k - (k%100))/100)
        f = (3*(tv**5) + 2*(tv**4) + 1734*(tv**3) + 14930*(tv**2) + 487*tv + 271*j*k + 2111*j + 1115*(k**2) + 3732*k + 83*(kk**2) + 68*kk + 73*l + 7*(dd3**2) + 658**dd3 + 131*(t**2) + 221*t + d4*t)%10000
        sk = str(f).zfill(4)

        kl03.append(sk)

    kl04 = []
    for t in range(6):
        tv = t + V
        j = ord((key[t]))
        k = ord(key[tv - 6])
        l = ord(key[int(V/2) + t - 3])
        kk = int((k - (k%100))/100)
        f = (2*(tv**5) + 7*(tv**4) + 3589*(tv**3) + 8951*(tv**2) + 248*tv + 63*j*k + 4421*j + 1718*(k**2) + 4487*k + 56*(kk**2) + 97*kk + 569*l + 12*(dd4**2) + 927**dd4 + 726*(t**2) + 1039*t + d0*t)%10000
        sk = str(f).zfill(4)

        kl04.append(sk)

    k00 = ''.join(kl00).zfill(24)
    k01 = ''.join(kl01).zfill(24)
    k02 = ''.join(kl02).zfill(24)
    k03 = ''.join(kl03).zfill(24)
    k04 = ''.join(kl04).zfill(24)

    K = [k00, k01, k02, k03, k04]
    D = lambda m: K[(int(K[m%5][m]) + int(K[(2*m + 2)%5][23 - m]))%5]

    klkl = []
    for n in range(24):
            
        kn = []
        for t in range(p[n]):
            tk = t + int(D(0)[n])
            k2 = ord(key[(p[n] - t - 1)%V])
            kk2 = int((k2 - (k2%100))/100)
            f2 = (tk**5 + tk**4 + (971 + int(D(1)[n]))*(tk**3) + (16947 - int(D(2)[n]))*(tk**2) + (2279+int(D(3)[n]))*tk + (282 - int(D(4)[n]))*(k2**2) + (4103+int(D(5)[n]))*k2 + kk2**2 + (194-int(D(6)[n]))*kk2 + 3411*n + 841*t*n + 7407*t + 5988)%10000
            sk2 = str(f2).zfill(4)
            kln = sk2[M[(11*n + n*t + 7*t + 5*int(D(7)[n]))%24][int(D(8)[n])%4]]
            kn.append(kln)

        klkl.append(''.join(kn))   

    C = ciphertext.replace(' ','').replace('\n','')

    LC = len(C)
    uetl = []
    for x in range(LC):
        l = ord(C[x])
        uetl.append(l)
    MM = max(uetl)
    mm = min(uetl)
    
    
    lxx = []
    for i in range(int(LC/3)):
        for j in range(24):
            lxx.append(str((int(D(9)[j])*p[1 + (i%23)] + 22*(i**2) + 13*i + 17*j)%10))

    G = 8*LC
    for i in range(G):
        for u in range(4):
            lxx[i] = str((int(lxx[i]) + int(lxx[(i + p[20 + u])%int(4*LC/12)]))%10)
            lxx[i] = str((int(lxx[(11527*(i - (int(D(10))%24)) + int(14029/(u + 1)))%G]) + ((i**2 + 12*i)*(u + 3)))%10)
    
    cq =[]
    for i in range(int(LC)):
        X = (int(D(11)[8] + D(12)[19]) + 5*i)%16
        W = str(bin(X)[2:].zfill(4))
        cq.append((int(str(lxx[4*i + int(W[0])]) + str(lxx[4*i + int(W[1]) + 1]) + str(lxx[4*i + int(W[2]) + 2]) + str(lxx[4*i + int(W[3]) + 3])) + int(D(13))%((27*i + 7)%(p[i%24]*p[(i+11)%24]) + 3))%24)
    
    Rb = []
    for i in range(LC):
        
        o = ord(C[i])
        g = int(D((2*i)%24) + D((2*i + 1)%24))%11172
        
        if g < 10000:
            if o - g < 44032:
                irsb = str(o - 44032).zfill(4)
            else:
                irsb = str(o - 45204).zfill(4)
        else:
            if (o - g)%2 == 0:
                irsb = str(int((o - g - 34032)/2)).zfill(4)
            else:
                irsb = str(int((o - g - 24031)/2)).zfill(4)
    
        m = []
        for w in range(4):
            m.append(irsb[Mr[cq[i]][w]])
        
        irs = ''.join(m)
        Rb.append(irs)
    
    Rc = ''.join(Rb)
    Rrb = Rc.replace('-', '0')
    R = list(Rrb)
    LR = len(R)
    
    for h in range(24):
        i = 23 - h
    
        e = i%6
        if e < 3:
            for j in range(LR):
                R[(17*i + j)%LR] = str((int(R[(17*i + j)%LR]) - (e - 3)*int(klkl[i][j%p[i]]))%10)
        else:
            for j in range(LR):
                R[(17*i - j)%LR] = str((int(R[(17*i - j)%LR]) - (e - 2)*int(klkl[i][j%p[i]]))%10)
    
    Ro = R
    for h in range(7):
        j = 6 - h
    
        for b in range(LR):
            i = LR - 1 - b
            Ro[i] = str((int(R[i]) - int(R[(i + j - p[23 - j] + 1)%LR]))%10)
            R[i] = str((int(Ro[i]) - int(Ro[(i - j - 1)%LR]))%10)
    
    Rx = []
    for i in range(LR):
        Rx.append(R[(i - int(klkl[0]))%LR])
    
    t = []
    for x in range(int(LR/6)):
        
        Y = []
        for j in range(6):
            Y.append(Rx[6*x + j])
        y = int(''.join(Y))
    
        for u in range(V):
            k3 = ord(key[u])
            stringkb = str(bin(k3**3 + 2*k3)[2:].zfill(47))
            stringko = str(oct(k3**3 + 2*k3)[2:].zfill(17))

        kv = ord(key[x%V])            
        z = int((902708 - 15394*((8*x)%11) - 9705*(6 - ((5*(x**2))%7)) - 7817*(12 - ((4*x)%13)) - 4211*(((3*(kv**2)) + 5*x)%16) + 2981*((kv%100)%5) - 2692*(22 - ((6*(x**2))%23)) + 179*((2*(kv**3))%37) - 41*(886 - (x%887)) + 17*(((x**4) - 19*(x**3) + 270*x)%643) + 129*(int(stringkb[(6*x)%47])) + 301*(int(stringko[16 - ((2*x)%17)]) + 2) - y)/(int(stringkb[46 - (x%47)]) + 1))

        t.append(chr(z))
    
    if '𱍊' in t:
        t.remove('𱍊')
    
    P = ''.join(t)
    
    return P

############### execution ###############

code = decrypt(
    '123456',
    '존렄촖쨌꺄촧쥚멇늁떒튻쩩며끏륂쬥뱏휜퉞뼯퇸벴극믺싷뿞빸해떔롱혁맋뀻헿딦괷춋껒댦뉅뻌톓캀쭻엮쀩퀫림뭏똰홒쏴퀓쎊쾒듟쪈묦 둶섉췑쉺쐲딫뱈쒓흛릢쁢록꺳쏭텽끛쳤럞덽룚춬쥅빂췔쿑헒엩씗캷세딎밹챑매쮳긨퀉뗚뎪뎨칇뚬뾷슮숑땲졷힚히딍졷튭퐲왹븣럒퀪뙃 퀔튋띡댸똫희즈왖쉾쿧뽈혢콧뱗섣냞폑끍훬띔켾츞즉급뤐볆퇎뇄휌뱣폂펏꺖좩귍처팋났뇍셔컂쨄핼딶굄콪놪뢦꿤쿢켓꼡맾톙틉탣꺆덪 긐졃뽀튧몆쇡맊퓥죧쉿줬츲왟굀툌뢡밃뷙'
)
exec(code)
