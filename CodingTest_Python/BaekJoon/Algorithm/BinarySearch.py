

## 1.iterative 한 이분탐색방법
# def binsearch(n,S,x):
#     low = 1
#     high = n
#     location = 0

#     while (low <= high and location == 0):
#         mid = (low+high) // 2
#         if x == S[mid]:
#             location == mid
#         elif x < S[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return location



# target = int(input())
# S = [-123,123,423,454,642,871,999,1000,1024,1045]

# result = binsearch(len(S)- 1,S,target)

# print(result)


## 2.Recursive한 이분탐색방법
# def bisearch2(S,low,high):
#     if low > high:
#         return 0

#     else:
#         mid = (low+high) // 2
#         print(low,mid,high)
#         if target == S[mid]:
#             return mid
#         elif target > S[mid]:
#             return bisearch2(S,mid+1,high)
#         else:
#             return bisearch2(S,low,mid-1)

# arr = list(map(int,input().split()))
# arr.sort()
# print(arr)
# #target = int(input())  
# target = int(input())


# print(bisearch2(arr,1,len(arr)-1))