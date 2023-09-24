import sys
input = sys.stdin.readline
from queue import PriorityQueue

V,E = map(int,input().split())
K = int(input())
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()


for _ in range(E):
    u,v,w = map(int,input().split())
    myList[u].append((v,w))

q.put((0,K))  
print(q)
distance[K] = 0

while q.qsize() >0:
    current = q.get()  # * current = (0,1) distance , node
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > value + distance[c_v]:
            distance[next] = value + distance[c_v]
            q.put((distance[next],next))


for i in range(1,V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
            
    
