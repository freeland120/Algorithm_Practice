a,b,c = map(int,input().split(" "))

ret1 = (a+b)%c
print(ret1)
ret2 = ((a%c)+(b%c))%c
print(ret2)
ret3 = (a*b)%c
print(ret3)
ret4 = ((a%c)*(b%c))%c
print(ret4)

