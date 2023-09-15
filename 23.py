n , m = map(int,input().split())
A = [[] for _ in range(n+1)]  #배열 안에 배열로 표현하면 된다. 
visited = [False] * (n+1) #0부터 시작하면 인덱스로 표현하기 힘들다. 그냥 과감히 인덱스1부터 넣는게 편하다. 

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


#인접리스트로 초기화하기  
for i in range(m):
    s,e = map(int,input().split()) #start index, end index 
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1,n+1): #인접리스트 방문하기
    if not visited[i]:
        count +=1
        DFS(i)

print(count)
