

a = int(input())

b = list(map(str,input()))

for i in range(3):
    print(a * int(b[2-i]))

new_b = int(b[0])*100 + int(b[1])*10 + int(b[2]) 

print(a*new_b)





# arr = []
# for _ in range(2):
#     x = input()
#     arr.append(x)

# for i in range(2,-1,-1):
#     if i <= 2:
#         result = int(arr[0]) * int(arr[1][i])
#         print(result)
#         if i == 0:     
#             result = int(arr[0])*int(arr[1])
#             print(result)
    



# a = int(input())
# b = list(map(int,list(input())))
# for i in range(3):
# 	print(a*b[2-i])
# print(a*(100*b[0]+10*b[1]+b[2]))




