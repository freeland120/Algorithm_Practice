# from collections import deque


# #BFS 메서드 정의
# def BFS(graph,start,visited):

#     #큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     #현재 노드를 방문 처리
#     visited[start] = True

#     #큐가 빌 때까지 반복
#     while queue:

#         #큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v,end=' ')

        
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True




# graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# visited = [0] * 9


# BFS(graph,1,visited)

###############################################################################################################



#<문제> 음료수 얼려먹기

def DFS(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:

        graph[x][y] = 1

        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False


N, M = map(int,input().split())


graph = []


for i in range(N):
    graph.append(list(map(int,input())))



result = 0

for i in range(N):
    for j in range(M):
        if DFS(i,j) == True:
            result += 1
print(result)


