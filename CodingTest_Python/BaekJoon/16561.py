




# #3의 배수
# #n은 3의 배수, count는 n을 분해하는 갯수라고 한다면...

# #n이 9일때는 1
# #n이 12일때는 3
# #n이 15일때는 6
# #n이 18일때는 10


# n = int(input())

# num = 1

# count = 2

# for i in range(9,n,3):
#     num = num + count
#     count += 1
# print(num)







n = int(input())


cnt = 0

for i in range(3,n+1,3):
    for j in range(3,n+1,3):
        for k in range(3,n+1,3):

            if i+j+k == n:
                cnt += 1
            elif (i+j+k)>n:
                break

print(cnt)        




























