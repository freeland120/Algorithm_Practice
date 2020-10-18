def start_num(x):
    ret = 0
    while(x > 0):
        ret = x % 10
        x //= 10
    return ret

n = int(input())
ans = 1
cnt = -1

for i in range(n):
    if(start_num(ans) == 1):
        cnt += 1
    ans *= 5

print("0.", end="")
for i in range(cnt):
    print(0, end="")
print(ans)