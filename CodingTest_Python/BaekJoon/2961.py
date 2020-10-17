



##여기까지가 공식
# select = []

# def recur(depth,start):


#     if depth == n:
#         print(select)
#         return
    

#     for i in range(start, k):
#         select.append(i)
#         recur(depth+1,i+1)
#         select.pop()



# k = int(input())


# #arr = list(map(int,input().split()))

# for n in range(1,k+1):
#     recur(0,0)


# #start는 이번 자리에 어떤 수부터 집어 넣을 거냐





##여기서부터 2961번의 풀이

# result = 10000000000

# def check():
#     global result
#     x = 1
#     y = 0
    
#     for i in select:
    
        
#         x *= arr[i][0]
#         y += arr[i][1]

#     result = min(result,abs(x-y))






# select = []

# def recur(depth,start):


#     if depth == n:
        
#         check()
#         return
    

#     for i in range(start, k):
#         select.append(i)
#         recur(depth+1,i+1)
#         select.pop()



# k = int(input())


# arr = []

# for i in range(k):
#     arr.append(list(map(int,input().split())))

# for n in range(1,k+1):

#     recur(0,0)

# print(result) 

########


answer = 10000000000000000

def recur(cur,cnt,x,y):
    global answer
    if cur == n:

        if cnt == 0:
            return
        answer = min(answer,abs(x-y))
    
        return

    recur(cur+1,cnt+1,x*arr[cur][0],y+arr[cur][1])
    recur(cur+1,cnt,x,y)


n = 4

arr = [[1,7],[2,6],[3,8],[4,9]]

recur(0,0,1,0)

print(answer)
























# def mix(sour,bitter,s,b):
#     global answer
#     if len(sour) == 0:
#         answer.append(abs(s-b))
#         return
    
#     for i in range(len(sour)):
        
#         mix(sour[i+1:],bitter[i+1:],s,b)
#         sTemp = s * sour[i]
#         bTemp = b + bitter[i]
#         mix(sour[i+1:],bitter[i+1:],sTemp,bTemp)


# n = int(input())


# sour = []
# bitter = []
# answer = []


# for _ in range(n):
#     s,b = map(int,input().split())
#     sour.append(s)
#     bitter.append(b)
    


# for i in range(n):
#     s = sour[i]
#     b = bitter[i]
#     mix(sour[i+1:],bitter[i+1:],s,b)


# print(min(answer))