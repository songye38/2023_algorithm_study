#####################
# 최소 신장 트리 구하기 
# 골드 4
# 백준 1197번
# 23.9.26
#####################

import sys
from queue import PriorityQueue
input = sys.stdin.readline


N,M = map(int,input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

#1 2 1
for _ in range(M):
    S,E,W = list(map(int,input().split()))
    pq.put((W,S,E))


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a !=b:
        parent[b] = a


useEdge = 0
result = 0

while useEdge < N-1:
    now = pq.get()
    if find(now[1]) != find(now[2]):
        union(now[1],now[2])
        result += now[0]
        useEdge+=1

print(result)

