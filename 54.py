from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
selfBuild = [0] * (N+1)


for i in range(1,N+1):
    #인접 리스트 저장
    time, *pre_buildings,_ = list(map(int,input().split()))
    selfBuild[i] = time # 자기 자신 시간 리스트 데이터 저장 
    if pre_buildings:
        for j in pre_buildings:
            A[j].append(i) #인접 리스트 저장
            indegree[i] +=1

queue = deque()

for i in range(1,N+1):
    if indegree[i] ==0:
        queue.append(i)

result = [0] * (N+1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -=1
        result[next] = max(result[next],result[now]+selfBuild[now])
        if indegree[next]==0:
            queue.append(next)


for i in range(1,N+1):
    print(result[i] + selfBuild[i])

