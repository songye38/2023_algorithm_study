from collections import deque

n = int(input())
A = [[0] for _ in range(n+1)]


for _ in range(n): #데이터 입력받기
    data = list(map(int,input().split()))
    index = 0
    s = data[index]
    index +=1
    while True:
        e = data[index]
        if e==-1:
            break
        v = data[index+1]
        A[s].append((e,v))
        index +=2

print("A",A)
distance = [0]*(n+1)
visited = [False]*(n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            print(i)



    
BFS(1)



#BFS(1)


     