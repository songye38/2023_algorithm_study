# 5 10 2
# 1 2 2 
# 1 3 7
# 1 4 5
# 1 5 6
# 2 4 2
# 2 3 4
# 3 4 6
# 3 5 8
# 5 2 4
# 5 4 1

import sys
input = sys.stdin.readline
from queue import PriorityQueue

N,M,K =map(int,input().split())
W = [[] for _ in range(N+1)]
distance = [[[sys.maxsize] * (K)] for i in range(N+1)]

for _ in range(M):
    s,e,v = list(map(int,input().split()))
    W[s].append((e,v))

q = PriorityQueue()
q.put((0,1))
distance[1][0] = 0


while q.qsize()>0:
    now = q.get()
    node = now[0]
    cost = now[1]
    for tmp in W[now]:
        new_distance = distance[node] + cost
        if distance[K][tmp[0]] > new_distance:
            distance[K][tmp[0]] = new_distance
            distance.sort()
            

for _ in range(len(N)):
    pass




