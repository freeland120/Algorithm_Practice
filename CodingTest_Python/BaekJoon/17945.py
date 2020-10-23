from math import sqrt

A, B = map(int, input().split())

a = 1
b = 2*A
c = B

r1 = (-b+sqrt(b*b-4*a*c))/(2*a)
r2 = (-b-sqrt(b*b-4*a*c))/(2*a)

r1 = int(round(r1))
r2 = int(round(r2))

if r1 == r2:
    print(r1)
else:
    if r1 > r2:
        r1, r2 = r2, r1
    
    print(r1, r2)