#####################
# 리프 노드의 개수 구하기 
# 실버 1
# 백준 1068
# 23.9.27
#####################

import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
visited = [False] * (N)
answer = 0
p = list(map(int,input().split()))

for i in range(N):
    if p[i] !=-1:
        tree[i].append(p[i])
        tree[p[i]].append(i)

    else: #-1 인 경우
        root = i

def DFS(number):
    global answer
    cNode = 0
    visited[number] = True
    for i in tree[number]:
        if not visited[i] and i !=deleteNode:
            cNode +=1
            DFS(i)
    if cNode == 0:
        answer += 1

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)

