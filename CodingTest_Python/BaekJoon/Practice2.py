
#1~n까지 k개를 뽑을때 "중복허용"한 조합(Combination) 만들기


def recur(depth,start):
    if depth == k:
        for i in range(k):
            print(arr[i],end=" ")
        print()
        return


    for i in range(start,n+1):
        
        arr.append(i)
        recur(depth+1,i)
        arr.pop()
        




n, k = map(int,input().split())

arr = []

recur(0,1)