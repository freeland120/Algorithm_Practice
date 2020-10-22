# 세 수



x,y,z = map(int,input().split())



if x+y == z:
    print("%d+%d=%d" %(x,y,z))
elif x-y == z or z == x-y:
    print("%d-%d=%d" %(x,y,z))
elif x*y == z or z == x*y:
    print("%d*%d=%d" %(x,y,z))
elif x/y == z:
    print("%d/%d=%d" %(x,y,z))
elif x == y+z:
    print("%d=%d+%d" %(x,y,z))
elif x == y-z:
    print("%d=%d-%d" %(x,y,z))
elif x == y*z:
    print("%d=%d*%d" %(x,y,z))
else:
    print("%d=%d/%d" %(x,y,z))




