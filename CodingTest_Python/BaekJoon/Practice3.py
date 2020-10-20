




# arr = [2,1,2,3,4,5,4,3]


# n = int(input())


# result  = n % 8

# print(arr[result])




# # a ^= b
# # b ^ = a
# # a ^= b

# a = 1
# a /= 3
# b = a
# c = a

# if a+b+c == 1:
#     print(1)
# else:
    # print(0)





def recur(depth):
    if depth == n:
       
        for i in arr:
            print(i,end=" ")
        print()
        return

    
    for i in range(k)[::-1]:
        arr.append(i)
        recur(depth+1)
        arr.pop()



n,k = map(int,input().split())

arr = []


recur(0)























