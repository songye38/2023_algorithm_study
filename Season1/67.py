#####################
# 트리의 부모 찾기 
# 실버 2
# 백준 11725
# 23.9.27
#####################

import sys
input = sys.stdin.readline

N = int(input())



visited = [False] * (N+1)
tree = [0 for _ in range(N+1)]
answer = [0] * (N+1)


for i in range(N-1):
    S,E = map(int,input().split())
    tree[S].append(E)
    tree[E].append(S)


#DFS
def DFS(now):
    visited[now] = True
    for next in tree[now]:
        answer[next] = now
        DFS(next)

DFS(1)
for i in range(2,N):
    print(answer[i])
