
# 괄호 없는 사칙연산

# import sys
# import math

# def solution(a,b,o):
    
    
#     if (a > 0 and b >0) or (a < 0 and b < 0):
#         result = {'+':a+b,'-':a-b,'*':a*b,'/':a//b}.get(o)
#         return result
#     elif (a > 0 and b <0) or (a < 0 and b > 0):
#         result = {'+':a+b,'-':a-b,'*':a*b,'/':math.ceil(a/b)}.get(o,break)
#         return result
    


# k1,o1,k2,o2,k3 = sys.stdin.readline().split()

# arr = []

# ans1 = solution(int(k1),int(k2),o1)
# final_ans1 = solution(ans1,int(k3),o2)

# arr.append(final_ans1)

# ans2 = solution(int(k2),int(k3),o2)
# final_ans2 = solution(int(k1),ans2,o1)

# arr.append(final_ans2)


# arr.sort()


# for i in arr:
#     print(i)








def solution(a,b,o):
    if o == '+':
        return int(a) + int(b)
    elif o == '-':
        return int(a) - int(b)
    elif o == '*':
        return int(a) * int(b)
    
    else:
        result = abs(int(a)) // abs(int(b))

        if int(a) < 0 and int(b) < 0:
            return result
        
        elif int(a) > 0 and int(b) >0:
            return result
        
        else:
            return -result



arr = list(input().split())

ans = []

var1 = solution(arr[0],arr[2],arr[1])

case1 = solution(var1,arr[4],arr[3])

ans.append(case1)

var2 = solution(arr[2],arr[4],arr[3])

case2 = solution(arr[0],var2,arr[1])

ans.append(case2)

ans.sort()


for i in ans:
    print(i)