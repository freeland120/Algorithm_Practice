
# def Pow(a,b):
#     if b == 0:
#         return 1
    
#     else:
#         temp = Pow(a,b//2)
#         if b % 2 == 0:
#             return temp*temp
#         else:
#             return temp*temp*a
        




# N = int(input())


# print(float(Pow(2,N)) ** -1)

def Pow(x):
    result = 0
    while(x > 0):
        result = x % 10
        x //= 10
    return result

N = int(input())
ans = 1
cnt = -1

for i in range(N):
    if(Pow(ans) == 1):
        cnt += 1
    ans *= 5


print("0.", end="")
for i in range(cnt):
    print(0, end="")
print(ans)