


arr = []
visited = []

#n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)
n = 0
def recur(cur):
    if cur == n:
        return

    for i in range(n):
        if visited[i]:
            continue
    
        visited[i] = True
        arr.append(i)
        recur(cur+1)
        arr.pop()
        visited[i] = False