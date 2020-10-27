n = var = int(input())

cnt = 0



while True:
    ret1 = n // 10
    ret2 = n % 10
    total = ret1 + ret2
    cnt += 1
    n = int(str(n%10) + str(total%10))

    if var == n:
        break

print(cnt)