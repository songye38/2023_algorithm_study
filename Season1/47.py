
from collections import deque

N,M = map(int,input().split())
A = [[] for _ in range(N+1)]
answer = [0] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v) #추가해주기
    visited[v] = True
    while queue:
        new_node = queue.popleft()
        for i in A[new_node]:
            if not visited[i]:
                visited[i] = True
                answer[i] +=1
                queue.append(i)

for i in range(M):
    s,e = map(int,input().split())
    A[s].append(e)

for i in range(1,N+1):
    visited = [False] * (N+1)
    BFS(i)

maxVal = 0
for i in range(1,N+1):
    maxVal = max(maxVal,answer[i])

for i in range(1,N+1):
    if maxVal == answer[i]:
        print(i,end=' ')
