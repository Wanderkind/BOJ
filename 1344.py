import math
def f():s=float(input())/100;return sum((1-s)**(18-i)*s**i*math.comb(18,i)for i in[0,1,4,6,8,9,10,12,14,15,16,18])
print(1-f()*f())
