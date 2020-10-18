import sys

arr = []


for _ in range(3):
    
    n = int(input())
    s = 0    
    for i in range(n):
        num = int(sys.stdin.readline())
        s += num

    if s > 0:
        arr.append("+")
        
    elif s == 0:
        arr.append("0")
        
    elif s < 0:
        arr.append("-")
        


for i in arr:
    print(i)
