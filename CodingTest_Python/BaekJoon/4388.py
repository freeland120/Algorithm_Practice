



# import sys



# while True:
#     a,b = map(int,sys.stdin.readline().split())
#     cnt = 0

#     if a == 0 and b == 0:
#         break

#     #두 수를 입력받았을 때, 끝자리부터 더해가면서 "올림"이 발생하면 카운트

#     for i in range(len(str(max(a,b)))+1):
#         x = a % 10
#         y = b % 10
#         if(x+y+i>=10):
#             cnt += 1
#             i = 1
#         else:
#             i = 0
        
#         a = a // 10
#         b = b // 10
    
#     print(cnt)






# a, b = map(int,input().split())
# cnt = 0

# a = a % 10
# b = b % 10

# if a+b > 9:
#     cnt +=1









def solution(num1,num2):
    return num1 % (10 ** num2) // (10 ** (num2-1))

while True:
    a,b = map(int,input().split())
    arr = [0,0]
    cnt = 0

    if a == 0 and b == 0:
        break

    for i in range(1,len(str(max(a,b)))+1):
        x = solution(a,i)
        y = solution(b,i)

        if (x+y+arr[0]) > 9:
            cnt += 1
            arr[0] = 1
        else:
            arr[1] = 0
    print(cnt)
