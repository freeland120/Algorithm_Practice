


# x_list = []
# y_list = []

# for i in range(3):
#     x,y = map(int,input().split())

#     x_list.append(x)
#     y_list.append(y)


# for i in range(3):
#     if x_list.count(x_list[i]) == 1:
#         x = x_list[i]
#     elif y_list.count(y_list[i]) == 1:
#         y = y_list[i]

# print(x,y)


#1종류만 홀수개가 있고, 나머지가 짝수 개가 있을 때 다 XOR연산을 하면 홀수개를 알 수 있다.


x = 0
y = 0


for _ in range(3):

    a,b = map(int,input().split(" "))
    
    x ^= a
    y ^= b

print(x,y)





