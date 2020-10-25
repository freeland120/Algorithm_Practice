

# # import sys


# # arr = []

# # ans = []

# # for i in range(0,32):
# #     arr.append(2 ** i)


# # n = int(sys.stdin.readline())

# # for _ in range(n):
# #     target = int(sys.stdin.readline())
# #     if target in arr:
# #         ans.append(1)       
# #     else:   
# #         ans.append(0)

# # for i in ans:
# #     print(i)




# n = int(input())


# for _ in range(n):
#     a = int(input())

#     if (a & -a) == a:
#         print(1)
#     else:
#         print(0)






cnt = 0

n = 12


while n != 0:

    n -= (n & -n)

    cnt += 1

print(cnt)








