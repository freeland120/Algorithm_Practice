import sys
while True:
    try:
        x,y = map(int,sys.stdin.readline().split())
        print(x+y)
    except:
        break