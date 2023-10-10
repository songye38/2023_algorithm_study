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


#union연산을 위해 대표노드값 초기화해주기 
for i in range(N+1):
    parent[i] = i

#1 2 1
for _ in range(M):
    S,E,W = list(map(int,input().split()))
    pq.put((W,S,E)) #! 우선순위 큐에서는 제일 앞에 있는 원소를 기준으로 정렬되므로 가중치 값을 제일 먼저 저장하기


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
    w,s,e = pq.get() #! 하나의 값을 뽑은 다음 인덱싱으로 접근하지 말고 개별 값으로 접근하기 
    if find(s) != find(e):
        union(s,e)
        result += w
        useEdge+=1

print(result)

