


a,b = map(int,input().split())


a = a - 1
b = b - 1 


width = abs(a // 4 - b // 4)

height = abs(a % 4 - b % 4)

print(width+height)