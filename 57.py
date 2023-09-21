import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

N = int(input())
M = int(input())
myList = [[] for _ in range(N+1)]
dist = [sys.maxsize] * (N+1)
visited = [False] * (N+1)
q = PriorityQueue()

for _ in range(M):
    u,v,w = list(map(int,input().split()))
    myList[u].append((v,w))

start_index,end_index = map(int,input().split())

def dijkstra(start,end):
    q.put((0,start))
    dist[start] = 0

    while q.qsize() > 0:
        now_node = q.get()
        now = now_node[1]
        if not visited[now]:
            visited[now] = True
            for n in myList[now]:
                if not visited[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] =dist[now] + n[1] 
                    q.put((dist[n[0]],n[0]))
    return dist[end]

print(dijkstra(start_index,end_index))