x = int(input())

while True:

    if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
        print(1)
        break
    else:
        print(0)
        break

