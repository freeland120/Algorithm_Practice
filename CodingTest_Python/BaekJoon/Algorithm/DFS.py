# DFS 메서드 정의


# def DFS(graph,v,visited):

#     #현재 노드를 방문 처리
#     visited[v] = True
#     print(v,end=' ')

#     #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             DFS(graph,i,visited)

# graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# visited = [0] * 9



# DFS(graph,1,visited)





# graph2 = []


# for i in range graph:





#문제
#10이하의 자연수 N을 입력받아 주사위를 N번 던져서 나올 수 있는 모든 경우를 출력하는 프로그램을 작성하시오
#입력 예 : 3



arr = []

def recur(depth):

    

    if depth == N:
        
        for i in arr:
            print(i, end = " ")
        print()
        return


    for i in range(1,7):
        arr.append(i)
        recur(depth+1)
        arr.pop()


N = int(input())





recur(0)











# def DFS(depth):
    
    
#     if depth > N:
#         for i in range(1,N+1):
#             print(arr[i])        


    
#     for j in range(1,N+1):
#         arr[depth+1] = j
#         DFS(depth + 1)





# N = int(input())
# arr = []

# DFS(0)






















