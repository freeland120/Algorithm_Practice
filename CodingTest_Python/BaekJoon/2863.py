

# A/C + B/D 위에 있는 숫자가 분자, 아래 있는 숫자가 분모


A,B = map(int,input().split())

C,D = map(int,input().split())


arr = []


arr.append(A/C + B/D)
arr.append(C/D + A/B)
arr.append(D/B + C/A)
arr.append(B/A + D/C)


arr_max = max(arr)

# arr_min = min(arr)
# print(arr)
# # if arr.count(arr_max) >= 1:
# #     print(arr_min)
# # else:
# #     print(arr_max)

result = arr.index(arr_max)

print(result)