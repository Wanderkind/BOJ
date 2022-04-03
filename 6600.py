import math
while 1:
    try:
        x1,y1,x2,y2,x3,y3=map(float,input().split())
        print(abs(round(math.pi*math.sqrt((x1-x3)**2+(y1-y3)**2)/math.sin(math.pi-abs(math.atan2(y1-y2,x1-x2)-math.atan2(y3-y2,x3-x2)-math.pi)),2)))
    except EOFError:
        break
