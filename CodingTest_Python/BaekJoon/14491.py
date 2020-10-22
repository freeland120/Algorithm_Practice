
# 9진수



T = int(input())

result = 0
cnt = 0
while T > 0:
    result += T % 9 * pow(10,cnt)

    T //= 9
    cnt += 1


print(result)