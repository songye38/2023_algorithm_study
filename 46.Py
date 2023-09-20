from collections import deque

N,M,K,X = map(int,input().split())
A = [[] for _ in range(N+1)]
answer = []
visited = [-1] * (N+1)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] +=1
    while queue:
        new_node = queue.popleft()
        for i in A[new_node]:
            if visited[i] == -1:
                visited[i] = visited[new_node] +1
                queue.append(i)

for _ in range(M):
    pass


BFS(X)


answer.sort()

