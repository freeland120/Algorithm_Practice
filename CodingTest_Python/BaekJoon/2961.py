



##여기까지가 공식
select = []

def recur(depth,start):


    if depth == n:
        print(select)
        return
    

    for i in range(start, k):
        select.append(i)
        recur(depth+1,i+1)
        select.pop()



k = int(input())


#arr = list(map(int,input().split()))

for n in range(1,k+1):
    recur(0,0)


#start는 이번 자리에 어떤 수부터 집어 넣을 거냐





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